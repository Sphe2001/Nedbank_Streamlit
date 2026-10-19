"""Streamlit Question 7 interface using the saved optimised classifier. Look and feel: design/demo.html."""
import io
import json
import time
from html import escape
import pandas as pd
import streamlit as st
import ui
from predictor import ROOT,COLS,LABELS,load_model,predict,validate

st.set_page_config(page_title='Banking demand forecast',page_icon='📊',layout='wide')
st.html(f'<style>{(ROOT/"style.css").read_text(encoding="utf-8")}</style>'+ui.HYDRATE+ui.SEG,unsafe_allow_javascript=True)
# Streamlit reruns the script on every action, so the first-load motion keys off a session flag.
first=not st.session_state.get('seen');st.session_state.seen=True

@st.cache_resource
def model():return load_model()

examples=pd.read_csv(ROOT/'examples/valid_features.csv')
evidence=json.loads((ROOT/'evidence/test_results.json').read_text())
passed=sum(c['passed'] for c in evidence['checks'])
ARROW=dict(type='primary',icon=':material/arrow_forward:',icon_position='right',width='stretch')
QUIET=dict(icon=':material/download:',on_click='ignore')

# Always rendered (lit only on first load): a conditional element would shift every later slot and make Streamlit
# repaint the whole page as new elements on the next rerun, the old copy fading below the new one.
st.html(f'<i class="intro-flag{" on" if first else ""}"></i>')
st.html(ui.topbar())
# Not st.empty(): that clears the slot on every rerun, so the hero and prediction were torn down and rebuilt on each
# input change. Unchanged markup is kept in the DOM; show_hero overwrites this element in place only when predicting.
hero=st.html(ui.hero(),unsafe_allow_javascript=True)
left,right=st.columns([4,8],gap='small')
frame=None;clicked=False;read_error=None
with left,st.container(key='panel'):
    st.html('<h2 class="panel-h" id="predict">Input</h2>')
    mode=st.radio('Input method',['Demonstration cases','Upload CSV','Manual entry'],horizontal=True,key='input_mode',label_visibility='collapsed')
    if mode=='Demonstration cases':
        case=st.selectbox('Case',['Valid low activity','Valid medium activity','Valid high activity','Invalid negative count'],key='demo_case')
        if case=='Invalid negative count':frame=pd.read_csv(ROOT/'examples/invalid_features.csv')
        else:frame=examples.iloc[['Valid low activity','Valid medium activity','Valid high activity'].index(case):][:1].copy()
        clicked=st.button('Predict demand',key='predict_demo',**ARROW)
        with st.expander('Inspect the input features'):
            st.dataframe(frame.T.rename(columns={frame.index[0]:'Value'}),width='stretch')
        st.html('<p class="hint">Invented values. No personal records.</p>')
    elif mode=='Upload CSV':
        with st.container(horizontal=True,key='dl_row'):
            st.download_button('Valid CSV template',examples.to_csv(index=False),'valid_features.csv','text/csv',**QUIET)
            st.download_button('Invalid demonstration',(ROOT/'examples/invalid_features.csv').read_bytes(),'invalid_features.csv','text/csv',**QUIET)
        uploaded=st.file_uploader('Feature CSV',type=['csv'],key='feature_csv')
        st.html('<p class="hint">Prepared customer features in the 55-feature schema, not raw bank statements. Up to 1,000 rows and 2 MB.</p>')
        text=st.text_area('Or paste CSV text',help='Use either the file upload or pasted CSV, not both.',key='pasted_csv',placeholder='month_01,month_02,…')
        clicked=st.button('Predict uploaded rows',key='predict_upload',**ARROW)
        st.html('<p class="hint">Synthetic data only: no names, IDs, account numbers or confidential records. Files stay in server memory and are not written to disk, though a hosted service still receives the bytes.</p>')
        if clicked:
            try:
                if uploaded is not None and text.strip():raise ValueError('Choose a file upload or pasted CSV, not both.')
                if uploaded is not None:
                    if uploaded.size>2*1024*1024:raise ValueError('File exceeds 2 MB.')
                    frame=pd.read_csv(uploaded)
                elif text.strip():
                    if len(text.encode())>2*1024*1024:raise ValueError('Pasted CSV exceeds 2 MB.')
                    frame=pd.read_csv(io.StringIO(text))
                else:raise ValueError('Upload a CSV or paste CSV text first.')
            except (ValueError,pd.errors.ParserError,pd.errors.EmptyDataError,UnicodeDecodeError):
                read_error='Could not read the input. Choose one valid UTF-8 CSV under 2 MB with the required feature columns.'
    else:
        profile=st.selectbox('Starting template',['Low activity','Medium activity','High activity'],key='manual_profile')
        ix=['Low activity','Medium activity','High activity'].index(profile)
        initial=pd.DataFrame({'Feature':COLS,'Value':examples.iloc[ix][COLS].to_numpy(dtype=float)})
        edited=st.data_editor(initial,disabled=['Feature'],hide_index=True,num_rows='fixed',width='stretch',height=320,key='manual_editor_'+str(ix))
        frame=pd.DataFrame([dict(zip(edited.Feature,edited.Value))])
        st.html('<p class="hint">Keep count_3m, count_6m and count_12m equal to their monthly sums. Blank optional financial or income values use the saved training imputer.</p>')
        clicked=st.button('Predict entered profile',key='predict_manual',**ARROW)
with right:pred=st.container()

st.html('<span class="anchor" id="guidance"></span>')
with st.expander('Feature guidance',key='sec_guidance'):
    st.write('month_01 through month_12 represent November 2014 through October 2015. Counts are nonnegative whole numbers. Amount and balance fields use ZAR. debit_share is between 0 and 1; flags use 0 or 1.')
    st.dataframe(pd.read_csv(ROOT/'feature_guidance.csv'),hide_index=True,width='stretch')
st.html('<span class="anchor" id="limits"></span>')
with st.expander('Model and limits',key='sec_limits'):
    st.markdown('''**Responsible use.** Academic demonstration using 2015 data. Model probabilities are uncalibrated estimates. Use for capacity-planning research only; do not use for lending, fraud allegations, service denial or eligibility decisions.

**Demand classes.** Low is 0-49, Medium 50-199 and High 200 or more future transactions, November 2015 to January 2016. The thresholds are project assumptions, not official bank workload categories.

**Pipeline.** The saved pipeline performs training-fitted median imputation, signed log transformation, scaling and classification. No models are trained during prediction. Historical accuracy does not establish reliability on current customers or measured service benefits. Missing months indicate zero observed records, not necessarily inactivity.

**Privacy.** Use synthetic examples on a public demo. Do not submit names, IDs, account numbers or confidential banking records. Files are processed in server memory and are not written to disk by this app. A hosted service still receives uploaded bytes.

**Provenance.** The unchanged assignment champion, selected on validation data. Confirm dataset/model reuse terms before publishing. The app bundle includes no raw records or real customer examples.''')
st.html('<span class="anchor" id="evidence"></span>')
with st.expander('Test evidence',key='sec_evidence'):
    detail=lambda c:' · '.join(str(x) for x in [c.get('predicted_class') or c.get('error'),c.get('probability')] if x)
    st.html('<ul class="checks evi">'+''.join(f'<li class="ok">{ui.ICO["tick"]}<span><b>{escape(c["case"])}</b> {escape(detail(c))}</span></li>' for c in evidence['checks'])
        +f'</ul><p class="hint">Recorded by <code>python test_app.py</code> through Streamlit AppTest. Model SHA-256 <code>{evidence["model_sha256"][:16]}…</code></p>')
st.html(ui.footer(passed,len(evidence['checks'])))

# The prediction renders last, into placeholders above, so the pipeline loader can play first.
action={'Demonstration cases':'Predict demand','Upload CSV':'Predict uploaded rows','Manual entry':'Predict entered profile'}[mode]
months=ui.months_of(frame)
def show_hero(**kw):hero.html(ui.hero(**kw),unsafe_allow_javascript=True)
def two(wide):return st.columns([7,5],gap='small') if wide else (None,st.container())

if clicked and (frame is not None or read_error):
    result=None;err=read_error
    if not err:
        # Model-free checks first, so the loader (pass or fail) shows before the first model load, which takes seconds.
        try:validate(frame)
        except ValueError as e:err=str(e)
    show_hero(scan=err is None)
    slot=pred.empty()  # the loader, then the result; leftover cards after it are hidden in style.css (.pipe)
    with slot.container():st.html(ui.head(ui.trust('Checks running…','quiet'))+ui.pipeline(err is not None))
    t=time.time()
    if not err:
        try:result=predict(frame,model())
        except ValueError as e:err=str(e)
    time.sleep(max(0,1.5-(time.time()-t)))
    with slot.container():
        if err:
            fail=None if read_error else ui.failed_check(err)
            show_hero(fresh=True)
            st.html(ui.head(ui.trust('Input could not be read' if read_error else f'{fail} of 5 checks passed','bad')))
            a,b=two(months is not None)
            if a:a.html(ui.observed(months))
            with b,st.container(key='fc_err'):
                st.html(ui.ERROR_LEAD);st.error(err);st.html(ui.ERROR_SUB)
            if fail is not None:st.html(ui.checks(fail,open_=True))
        elif len(result)==1:
            row=result.iloc[0];k=LABELS.index(row.predicted_class)
            p=[row.low_probability,row.medium_probability,row.high_probability]
            show_hero(lit=[k],fresh=True)
            with st.container(horizontal=True,key='pred_head'):
                st.html(ui.head(),width='content');st.success('5 of 5 checks passed · uncalibrated',icon=':material/check:')
            a,b=st.columns([7,5],gap='small')
            a.html(ui.observed(months))
            with b,st.container(key=f'fc{k}'):
                with st.container(key='fc_cls'):st.metric('Predicted class',row.predicted_class,label_visibility='collapsed')
                with st.container(key='fc_pv'):st.metric('Model probability',f'{row.probability:.1%}',label_visibility='collapsed')
                st.html(ui.statement(k)+ui.COUNT_UP,unsafe_allow_javascript=True)
                st.html(ui.tile_foot(k))
            c,d=st.columns([7,5],gap='small')
            c.html(ui.chance(p,k));d.html(ui.last_quarter(ui.quarter_sum(months),k))
            st.html(f'<p class="note">{escape(row.explanation)}</p>'+ui.checks())
            st.download_button('Download predictions',result.to_csv(index=False),'predictions.csv','text/csv',**QUIET)
        else:
            names=[LABELS.index(c) for c in result.predicted_class]
            show_hero(lit=sorted(set(names)),fresh=True)
            with st.container(horizontal=True,key='pred_head'):
                st.html(ui.head(),width='content');st.success('Every row passed the checks',icon=':material/check:')
            with st.container(key='w_batch'):
                st.html(ui.batch_head([ui.CLASSES[i][0] for i in names]))
                probs=['probability','low_probability','medium_probability','high_probability']
                view=result[['row']].assign(predicted_class=[f'{ui.CLASSES[i][0]} {ui.CLASSES[i][1]}' for i in names],
                    **{c:result[c]*100 for c in probs},aug_oct=pd.to_numeric(frame['count_3m']).to_numpy())
                pc=lambda t:st.column_config.NumberColumn(t,format='%.1f%%')
                st.dataframe(view,hide_index=True,width='stretch',column_config={'row':'Row','predicted_class':'Predicted class','probability':pc('Probability'),
                    'low_probability':pc('Low'),'medium_probability':pc('Medium'),'high_probability':pc('High'),'aug_oct':'Aug–Oct'})
                st.download_button('Download predictions',result.to_csv(index=False),'predictions.csv','text/csv',**QUIET)
else:
    # One container, the same shape as Predict's slot, so the leftover cards land after the loader where CSS hides them.
    with pred.container():
        st.html(ui.head(ui.trust('Checks run when you predict','quiet')))
        a,b=two(months is not None and mode!='Upload CSV')
        if a:a.html(ui.observed(months))
        b.html(ui.idle(action))
