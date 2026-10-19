"""HTML and SVG pieces for the Count chart design. design/demo.html is the reference mock."""
import math
from html import escape

import pandas as pd

from predictor import MONTHS

CLASSES=[('Low','0–49',0,49),('Medium','50–199',50,199),('High','200+',200,None)]
MON='NDJFMAMJJASO'
CHECKS=['55 required features present','No extra or identifier columns','Counts are whole numbers of 0 or more',
    'Flags are 0 or 1, debit share within 0–1','Rolling counts equal monthly sums']
WARN='Academic demo on 2015 data. Probabilities are uncalibrated; not for decisions about real customers.'

def svgx(markup):
    """st.html sanitizes with DOMPurify's HTML-only profile, which drops every <svg>. SVG travels escaped in a
    data attribute instead, and HYDRATE (injected once with the stylesheet) puts it back."""
    return f'<span class="svgx" data-svg="{escape(markup)}"></span>'
HYDRATE='''<script>(()=>{if(window.__svgx)return;window.__svgx=1;
const fill=n=>{if(n.nodeType!==1)return;for(const e of [n,...n.querySelectorAll('[data-svg]')])if(e.dataset&&e.dataset.svg!==undefined){e.innerHTML=e.dataset.svg;delete e.dataset.svg}};
fill(document.body);new MutationObserver(ms=>{for(const m of ms)m.addedNodes.forEach(fill)}).observe(document.body,{childList:true,subtree:true})})()</script>'''
# Fluid seg: the highlighter flows between options instead of sliding. Each edge is a spring towards its new spot, the
# leading edge stiff and quick, the trailing edge softer, so the pill stretches into the move, thins a little like a
# drop, and draws itself back together as it lands. Lives outside React's render, so it re-finds the radiogroup after
# every rerun and keeps the last spot in `last`. No "<" before a letter or digit anywhere: DOMPurify would read it as a
# tag (checked in __main__).
SEG='''<script>(()=>{if(window.__seg)return;window.__seg=1;
const Q='.st-key-input_mode [role="radiogroup"]',rm=matchMedia('(prefers-reduced-motion: reduce)');let last=null,anim=null;
const box=(g,l)=>{const a=g.getBoundingClientRect(),b=l.getBoundingClientRect();return{x:b.left-a.left,y:b.top-a.top,w:b.width,h:b.height}};
const put=(e,r)=>{e.style.transform=`translate(${r.x}px,${r.y}px)`;e.style.width=r.w+'px';e.style.height=r.h+'px'};
// Spring progress 0..1 sampled into N+1 frames over D ms (omega w, damping z, held still for the first `hold` ms);
// the last frame lands exactly. The trailing edge holds briefly, as if surface tension kept it, then catches up.
const D=600,N=48,spring=(w,z,hold=0)=>{const o=[];let x=0,v=0;for(let i=0;i<=N;i++){o.push(x);if(i*D/N>=hold)for(let k=8;k--;){v+=(w*w*(1-x)-2*z*w*v)*D/N/8e3;x+=v*D/N/8e3}}o[N]=1;return o};
const LEAD=spring(21,.82),TRAIL=spring(16,1,45);
const mount=g=>{const ind=document.createElement('i'),hov=document.createElement('i');ind.className='seg-ind';hov.className='seg-hov';
for(const e of [hov,ind]){e.setAttribute('aria-hidden','true');g.append(e)}
g.addEventListener('pointerover',ev=>{const l=ev.target.closest('label');if(!l||!g.contains(l))return;
if(l.matches('[data-selected="true"]')){hov.classList.remove('on');return}
if(!hov.classList.contains('on')){hov.classList.add('jump');put(hov,box(g,l));hov.offsetWidth;hov.classList.remove('jump')}else put(hov,box(g,l));hov.classList.add('on')});
g.addEventListener('pointerleave',()=>hov.classList.remove('on'));g.addEventListener('click',()=>hov.classList.remove('on'));
new ResizeObserver(()=>{const on=g.querySelector('label[data-selected="true"]');if(on&&!anim){last=box(g,on);put(ind,last)}}).observe(g);return ind};
const sync=()=>{const g=document.querySelector(Q);if(!g)return;const ind=g.querySelector(':scope>.seg-ind')||mount(g);
const on=g.querySelector('label[data-selected="true"]');if(!on)return;const r=box(g,on),p0=last;last=r;
if(!p0||(p0.x===r.x&&p0.w===r.w)||!ind.isConnected){put(ind,r);return}
// A switch mid-flow starts from wherever the pill is now, not from where it was heading.
const p=anim?box(g,ind):p0;if(anim)anim.cancel();put(ind,r);
if(rm.matches)anim=ind.animate([{opacity:0},{opacity:1}],{duration:220,easing:'ease-out'});else{
// a: trailing edge, b: leading edge. The pill thins as it stretches past its resting width, as a drop would.
const s=r.x>p.x,a0=s?p.x:p.x+p.w,a1=s?r.x:r.x+r.w,b0=s?p.x+p.w:p.x,b1=s?r.x+r.w:r.x,m=r.y+r.h/2;
anim=ind.animate(LEAD.map((e,i)=>{const t=TRAIL[i],a=a0+(a1-a0)*t,b=b0+(b1-b0)*e,w=Math.abs(b-a),rest=p.w+(r.w-p.w)*(e+t)/2,
h=(p.h+(r.h-p.h)*t)*Math.min(1,Math.max(.84,(rest/w)**.25));return{transform:`translate(${Math.min(a,b)}px,${m-h/2}px)`,width:w+'px',height:h+'px'}}),D)}
const cur=anim;cur.finished.then(()=>{if(anim===cur)anim=null},()=>{})};
let q=0;const soon=()=>{if(!q)q=requestAnimationFrame(()=>{q=0;sync()})};
new MutationObserver(soon).observe(document.body,{childList:true,subtree:true,attributes:true,attributeFilter:['data-selected']});soon()})()</script>'''
def svg(body):return svgx(f'<svg viewBox="0 0 24 24" aria-hidden="true">{body}</svg>')
ICO={'tick':svg('<path d="M5 12.5l4.5 4.5L19 7.5"/>'),'cross':svg('<path d="M6.5 6.5l11 11M17.5 6.5l-11 11"/>'),
    'dash':svg('<path d="M7 12h10"/>'),
    'sliders':svg('<path d="M4 7h9M17 7h3M4 12h3M11 12h9M4 17h11M19 17h1"/><circle cx="15" cy="7" r="2"/><circle cx="9" cy="12" r="2"/><circle cx="17" cy="17" r="2"/>'),
    'tree':svg('<path d="M12 3l-6 8h3.5L5 17h14l-4.5-6H18z"/><path d="M12 17v4"/>')}
SLIP='M.5 .5h6.2l2.8 2.8v10.2H.5z'

def num(v):
    v=float(v);return f'{int(v):,}' if v.is_integer() else f'{v:,.1f}'
def pct(p):return f'{p*100:.1f}%'
def words(text,base=0):
    return ' '.join(f'<span class="rw"><span style="--i:{i+base}">{escape(w)}</span></span>' for i,w in enumerate(text.split()))
def per_month(k):
    lo,hi=CLASSES[k][2],CLASSES[k][3]
    if hi is None:return f'about {math.ceil(lo/3)}+ a month'
    return f'up to about {round(hi/3)} a month' if lo==0 else f'about {round(lo/3)}–{round(hi/3)} a month'

def months_of(frame):
    """The twelve monthly counts of a one-row frame, or None when there is nothing to draw."""
    if frame is None or len(frame)!=1 or not set(MONTHS)<=set(frame.columns):return None
    m=pd.to_numeric(frame.iloc[0][MONTHS],errors='coerce').astype(float).tolist()
    return None if all(math.isnan(v) for v in m) else m
def quarter_sum(m):return sum(v for v in m[-3:] if not math.isnan(v))

def topbar():
    mark=''.join(f'<path d="{SLIP}" transform="translate({x} {y}) scale(.75 .786)" style="fill:var(--c{i})"/>' for i,(x,y) in enumerate([(0,7),(9,3.5),(18,0)]))
    nav=''.join(f'<a href="#{a}"{" aria-current=page" if not i else ""}>{t}</a>' for i,(a,t) in enumerate(
        [('predict','Predict'),('guidance','Feature guidance'),('limits','Model and limits'),('evidence','Test evidence')]))
    mark=svgx(f'<svg width="26" height="22" viewBox="0 0 26 22" aria-hidden="true">{mark}</svg>')
    return f'''<header class="top"><div class="brand">{mark}Banking demand forecast</div>
<nav class="nav" aria-label="Sections">{nav}</nav><span class="scope">IDA117V · Question 7</span></header>'''

def hero(lit=(),scan=False,fresh=False):
    """The three classes sweep while the pipeline runs; the predicted ones fill when it answers."""
    cls=[f'<span class="cls{" on" if i in lit else ""}" style="--k:{i};--cc:var(--c{i})" data-t="{n}">{n}</span>' for i,(n,*_) in enumerate(CLASSES)]
    state=''.join(c for c,on in [(' scan',scan),(' fresh',fresh)] if on)
    # The markup must not change between reruns, or Streamlit rebuilds the hero; the breath phase is set here instead.
    return f'''<section class="hero{state}"><img src="app/static/hero.jpg" alt="" width="2400" height="786">
<div class="hero-copy"><h1>{words("Banking demand forecast")}</h1>
<p>{cls[0]}, {cls[1]} or {cls[2]} demand for <b>November 2015 to January 2016</b>.</p></div></section>
<script>(()=>{{for(const h of document.querySelectorAll('.hero'))h.style.setProperty('--t',performance.now()|0);if(window.__lean||matchMedia('(prefers-reduced-motion: reduce)').matches||!matchMedia('(pointer: fine)').matches)return;window.__lean=1;
const set=(h,x,y)=>{{h.style.setProperty('--px',x);h.style.setProperty('--py',y)}};
addEventListener('pointermove',e=>{{const h=e.target.closest&&e.target.closest('.hero');if(!h)return;const r=h.getBoundingClientRect();
set(h,((e.clientX-r.left)/r.width-.5).toFixed(3),((e.clientY-r.top)/r.height-.5).toFixed(3))}});
addEventListener('pointerout',e=>{{const h=e.target.closest&&e.target.closest('.hero');if(h&&!h.contains(e.relatedTarget))set(h,0,0)}})}})()</script>'''

def timeline(m):
    """Twelve monthly bars on one scale (0-120 unless a month runs higher), Aug-Oct bracketed."""
    W,H,L,R,T,B=460,170,30,4,44,26
    seen=[v for v in m if not math.isnan(v)];mx=120*max(1,math.ceil(max(seen+[0])/120))
    neg=18 if any(v<0 for v in seen) else 0;zero=H-B-neg
    y=lambda v:zero-(min(v,mx)/mx)*(zero-T)
    step=(W-L-R)/12;bw=step*.62;bx=lambda i:L+step*i+(step-bw)/2
    g=''.join(f'<line class="grid" x1="{L}" x2="{W-R}" y1="{y(v):.1f}" y2="{y(v):.1f}"/><text class="ax" x="{L-8}" y="{y(v)+4:.1f}" text-anchor="end">{v}</text>' for v in range(0,mx+1,mx//3))
    for i,v in enumerate(m):
        x=bx(i)
        if math.isnan(v):pass
        elif v>=0:g+=f'<rect class="tl-bar{" q" if i>8 else ""}" style="--i:{i}" x="{x:.1f}" y="{y(v):.1f}" width="{bw:.1f}" height="{max(2,zero-y(v)):.1f}" rx="{min(6,bw/2):.1f}"/>'
        else:g+=f'<rect class="tl-bar neg" style="--i:{i}" x="{x:.1f}" y="{zero}" width="{bw:.1f}" height="12" rx="4"/><text class="tl-neg" x="{x+bw/2:.1f}" y="{zero+26}" text-anchor="middle">{num(v)}</text>'
        g+=f'<text class="ax" x="{x+bw/2:.1f}" y="{H-6}" text-anchor="middle">{MON[i]}</text>'
    q=quarter_sum(m);top=min([y(max(v,0)) for v in m[9:] if not math.isnan(v)]+[zero])-14
    x0,x1=bx(9),bx(11)+bw;lbl=f'Aug–Oct · {num(q)}';pw=len(lbl)*7+24;cx=(x0+x1)/2
    g+=f'<path class="tl-br" d="M{x0:.1f} {top+6:.1f}V{top:.1f}H{x1:.1f}V{top+6:.1f}"/><rect class="tl-pill" x="{cx-pw/2:.1f}" y="{top-32:.1f}" width="{pw}" height="24" rx="12"/><text class="tl-pt" x="{cx:.1f}" y="{top-15.5:.1f}" text-anchor="middle">{lbl}</text>'
    return svgx(f'<svg class="chart" viewBox="0 0 {W} {H}" role="img" aria-label="Monthly transactions, November 2014 to October 2015. August to October total: {num(q)}.">{g}</svg>')

def quarter(q,k):
    """The August-October count laid against the class thresholds."""
    W,H,L,R,mx=340,88,4,4,400
    x=lambda v:L+(min(max(v,0),mx)/mx)*(W-L-R)
    g='';hit=-1
    for i,(a,b) in enumerate([(0,50),(50,200),(200,400)]):
        clash=x(a)<=x(q)<x(a)+len(CLASSES[i][0])*7+16  # the marker would cut through this band's label
        if clash:hit=i
        g+=f'<rect class="qb{" on" if i==k else ""}" x="{x(a):.1f}" y="40" width="{x(b)-x(a)-3:.1f}" height="22" rx="11"/>'
        if not clash:g+=f'<text class="qbl{" on" if i==k else ""}" x="{x(a)+11:.1f}" y="55">{CLASSES[i][0]}</text>'
    g+=''.join(f'<text class="ax" x="{x(v):.1f}" y="82">{v}</text>' for v in (0,50,200))+f'<text class="ax" x="{W-R}" y="82" text-anchor="end">400+</text>'
    qx=x(q);anchor='end' if qx>W*.72 else 'start' if qx<70 else 'middle'
    g+=f'<line class="qm" x1="{qx:.1f}" x2="{qx:.1f}" y1="26" y2="66"/><circle class="qd" cx="{qx:.1f}" cy="26" r="5"/><text class="qt" x="{qx:.1f}" y="13" text-anchor="{anchor}">Aug–Oct: {num(q)}{" · "+CLASSES[hit][0] if hit>=0 else ""}</text>'
    return svgx(f'<svg class="chart" viewBox="0 0 {W} {H}" role="img" aria-label="August to October 2015 observed: {num(q)} transactions, against class thresholds 50 and 200">{g}</svg>')

def head(trust_html=''):
    return f'<div class="pred-head"><h2>{svgx(f"<svg viewBox=\"0 0 10 14\" aria-hidden=\"true\"><path d=\"{SLIP}\"/></svg>")}Prediction</h2>{trust_html}</div>'
def trust(text,kind=''):
    icon={'':ICO['tick'],'bad':ICO['cross']}.get(kind,'')
    return f'<p class="trust {kind}">{icon}<span>{escape(text)}</span></p>'
FOOT='<div class="fc-foot"><span class="pill">Forecast</span><span class="pill">Nov 2015 – Jan 2016</span></div>'

def observed(m,i=0):
    avg=round(sum(v for v in m if not math.isnan(v))/12)
    return f'<section class="w" style="--i:{i}"><div class="w-top"><span>Observed</span><span class="pill">Nov 2014 – Oct 2015</span></div><p class="big">{avg}<small>a month on average</small></p>{timeline(m)}</section>'
def idle(action):
    return f'<section class="w fc idle" style="--i:1"><p class="fc-none">No forecast yet</p><p class="fc-sub">Select {escape(action)} to run the saved pipeline.</p>{FOOT}</section>'

def statement(k):
    """The forecast tile's sentence. The number above it is the probability metric; the class metric sits in the DOM, visually hidden."""
    return f'<p class="fc-stmt">chance of<b>{words(CLASSES[k][0]+" demand")}</b></p>'
def tile_foot(k):return f'<p class="fc-sub">{CLASSES[k][1]} transactions · {per_month(k)}</p>{FOOT}'
# Scripts must not contain '<' before a letter, digit, '/' or '!': DOMPurify drops any text-only element whose
# content matches /<[/\w!]/, so 'e<1' or '<small>' would silently remove the whole <script>. ui.py's self-check guards this.
COUNT_UP='''<script>(()=>{let tries=0;
const go=()=>{const v=document.querySelector('.st-key-fc_pv [data-testid="stMetricValue"]');if(!v){if(20>tries++)requestAnimationFrame(go);return}
if(v.dataset.rolled)return;v.dataset.rolled=1;let n=v;while(n.firstElementChild)n=n.firstElementChild;
const end=n.textContent.replace('%',''),to=parseFloat(end),pct=document.createElement('small');pct.textContent='%';
const put=x=>{n.textContent=x;n.append(pct)};if(isNaN(to))return;
if(matchMedia('(prefers-reduced-motion: reduce)').matches)return put(end);
const t0=performance.now(),roll=t=>{const e=1-Math.pow(1-Math.min(1,(t-t0)/700),3);put(1>e?(to*e).toFixed(1):end);if(1>e)requestAnimationFrame(roll)};requestAnimationFrame(roll)};go()})()</script>'''

ERROR_LEAD='<p class="fc-none">No forecast</p>'
ERROR_SUB=f'<p class="fc-sub">Nothing was sent to the model. Correct the input and predict again.</p>{FOOT}'

def chance(p,k):
    rows=''.join(f'''<li class="{"on" if i==k else ""}"><span class="nm">{n}{'<span class="tag">Predicted</span>' if i==k else ""}<small>{r} transactions</small></span>
<span class="tr"><i style="--i:{i};width:{p[i]*100:.1f}%;background:var(--c{i})"></i></span><span class="v">{pct(p[i])}</span></li>''' for i,(n,r,*_) in enumerate(CLASSES))
    return f'<section class="w" style="--i:2"><div class="w-top"><span>Chance by class</span><span class="pill">uncalibrated</span></div><ul class="oc">{rows}</ul></section>'
def last_quarter(q,k):
    return f'''<section class="w" style="--i:3;--c-on:var(--c{k})"><div class="w-top"><span>Last quarter</span><span class="pill">Aug–Oct 2015</span></div>
<p class="big">{num(q)}<small>transactions</small></p>{quarter(q,k)}<p class="w-note">Laid against the class thresholds as context, not a cause.</p></section>'''
def batch_head(classes):
    counts=', '.join(f'{classes.count(n)} {n}' for n,*_ in CLASSES if n in classes)
    return f'<div class="w-top"><span>Uploaded rows</span><span class="pill">Nov 2015 – Jan 2016</span></div><p class="big">{len(classes)}<small>row{"s" if len(classes)!=1 else ""} predicted · {counts}</small></p>'

def failed_check(msg):
    """Which of CHECKS a predictor.validate message belongs to. validate() runs them in this order."""
    if 'extra columns' in msg:return 1
    if 'must be 0 or 1' in msg or 'must lie between' in msg:return 3
    if msg.startswith('count_') and ('must equal the sum' in msg or msg.endswith('is required.')):return 4
    if any(s in msg for s in ('cannot be negative','whole counts','must contain numbers','must be finite','monthly counts are required')):return 2
    return 0
def checks(fail=None,open_=False):
    """Checks before the failing one passed, the failing one failed, later ones were never reached."""
    items=''
    for i,t in enumerate(CHECKS):
        state='ok' if fail is None or i<fail else 'bad' if i==fail else 'skip'
        note={'ok':'','bad':'','skip':' (not reached)'}[state]
        items+=f'<li class="{state}">{ICO[{"ok":"tick","bad":"cross","skip":"dash"}[state]]}<span>{t}{note}</span></li>'
    return f'<details class="ck"{" open" if open_ else ""}><summary>All input checks</summary><ul class="checks">{items}</ul></details>'

def pipeline(bad):
    steps=[('Validate inputs','tick',18,0),('Preprocess','sliders',50,380),('Random Forest','tree',82,760)]
    track=''.join(f'<div class="pipe-step{" bad" if bad and i==0 else " off" if bad else ""}" style="left:{l}%;--d:{d}ms"><b>{ICO["cross" if bad and i==0 else ic]}</b><span>{t}</span></div>' for i,(t,ic,l,d) in enumerate(steps))
    big,sub=('Checking the input…','A check failed, so the model will not run.') if bad else ('Running the saved pipeline…','Validation, imputation and scaling, then 260 trees vote.')
    return f'''<section class="pipe" aria-live="polite"><p class="pipe-lbl">Data processing</p><div class="pipe-track"><i class="pipe-fill{" stop" if bad else ""}"></i>{track}</div>
<div><p class="pipe-big">{big}</p><p class="pipe-sub">{sub}</p></div></section>'''

def footer(passed,total):
    return f'''<footer class="foot"><div class="foot-row"><span>{WARN}</span><a href="#evidence">{passed}/{total} tests pass</a></div>
<p class="wordmark" aria-hidden="true">Demand forecast</p></footer>'''

if __name__=='__main__':
    assert per_month(0)=='up to about 16 a month' and per_month(1)=='about 17–66 a month' and per_month(2)=='about 67+ a month'
    assert [failed_check(m) for m in ['month_01 cannot be negative.','Missing required features: month_01','Remove extra columns, including any identifiers or personal data: x',
        'income_missing must be 0 or 1.','count_3m must equal the sum of its last 3 monthly counts.','count_6m is required.','All 12 monthly counts are required.','debit_share must lie between 0 and 1.']]==[2,0,1,3,4,4,2,3]
    m=[-4.0]+[8.0]*11;assert quarter_sum(m)==24 and 'tl-bar neg' in timeline(m) and 'Aug–Oct · 24' in timeline(m) and '<svg' not in timeline(m)
    from html import unescape
    assert 'Aug–Oct: 24 · Low' in unescape(quarter(24,0)) and 'Aug–Oct: 330<' in unescape(quarter(330,2)) and 'Medium' in batch_head(['Low','Medium','High'])
    import re
    for js in (HYDRATE,SEG,COUNT_UP,hero()[hero().index('<script>'):]):
        assert not re.search(r'<[/\w!]',js.removeprefix('<script>').removesuffix('</script>')),'DOMPurify would drop this script'
    print('ui ok')
