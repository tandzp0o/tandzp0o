<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lê Trương Trọng Tấn — Fullstack Developer</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700;800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root{
    --bg: #0d1117;
    --bg-elev: #12181f;
    --panel: #161d26;
    --border: #232b36;
    --text: #e6edf3;
    --text-muted: #8b949e;
    --violet: #a78bfa;
    --violet-dim: #7c6fd1;
    --violet-glow: rgba(167,139,250,.18);
    --g1: #0e4429;
    --g2: #006d32;
    --g3: #26a641;
    --g4: #39d353;
    --mono: 'JetBrains Mono', monospace;
    --sans: 'Inter', sans-serif;
    --radius: 10px;
  }
  *{box-sizing:border-box; margin:0; padding:0;}
  html{scroll-behavior:smooth;}
  body{
    background:var(--bg);
    color:var(--text);
    font-family:var(--sans);
    line-height:1.6;
    overflow-x:hidden;
  }
  body::before{
    content:"";
    position:fixed; inset:0;
    background-image:
      linear-gradient(var(--border) 1px, transparent 1px),
      linear-gradient(90deg, var(--border) 1px, transparent 1px);
    background-size: 64px 64px;
    opacity:.25;
    pointer-events:none;
    z-index:0;
  }
  a{color:inherit; text-decoration:none;}
  ::selection{ background:var(--violet-glow); color:var(--text); }

  .wrap{ max-width:920px; margin:0 auto; padding:0 24px; position:relative; z-index:1;}

  /* ---------- NAV ---------- */
  nav{
    position:sticky; top:0; z-index:10;
    backdrop-filter: blur(10px);
    background:rgba(13,17,23,.75);
    border-bottom:1px solid var(--border);
  }
  nav .wrap{ display:flex; align-items:center; justify-content:space-between; padding:16px 24px;}
  .brand{ font-family:var(--mono); font-weight:700; font-size:15px; display:flex; align-items:center; gap:8px;}
  .brand .dot{ width:9px; height:9px; border-radius:50%; background:var(--g4); box-shadow:0 0 8px var(--g4); animation:pulse 2s infinite;}
  @keyframes pulse{ 0%,100%{opacity:1;} 50%{opacity:.35;} }
  .navlinks{ display:flex; gap:22px; font-family:var(--mono); font-size:13px; color:var(--text-muted);}
  .navlinks a:hover{ color:var(--violet); }
  @media (max-width:640px){ .navlinks{ display:none; } }

  /* ---------- HERO ---------- */
  header.hero{ padding:80px 0 60px; position:relative;}
  .hero-grid{ display:grid; grid-template-columns: 1.3fr .8fr; gap:40px; align-items:center;}
  @media (max-width:760px){ .hero-grid{ grid-template-columns:1fr; } }

  .eyebrow{
    font-family:var(--mono); font-size:12px; color:var(--g4);
    letter-spacing:.08em; margin-bottom:14px; display:flex; align-items:center; gap:8px;
  }
  .eyebrow::before{ content:"●"; font-size:9px; }

  .terminal{
    background:var(--panel);
    border:1px solid var(--border);
    border-radius:var(--radius);
    overflow:hidden;
    box-shadow:0 20px 60px -20px rgba(0,0,0,.6);
  }
  .terminal-bar{
    display:flex; align-items:center; gap:7px;
    padding:11px 14px; border-bottom:1px solid var(--border);
    background:var(--bg-elev);
  }
  .terminal-bar span{ width:11px; height:11px; border-radius:50%; }
  .terminal-bar span:nth-child(1){ background:#ff5f56;}
  .terminal-bar span:nth-child(2){ background:#ffbd2e;}
  .terminal-bar span:nth-child(3){ background:#27c93f;}
  .terminal-title{ margin-left:auto; margin-right:auto; font-family:var(--mono); font-size:12px; color:var(--text-muted);}
  .terminal-body{ padding:22px 20px; font-family:var(--mono); font-size:15px; min-height:190px;}
  .terminal-body .line{ margin-bottom:6px; }
  .prompt{ color:var(--g4); }
  .cmd{ color:var(--text); }
  .out-name{ color:var(--violet); font-weight:700; font-size:22px; display:block; margin:10px 0 4px;}
  .out-title{ color:var(--text-muted); }
  .cursor{ display:inline-block; width:8px; height:16px; background:var(--violet); vertical-align:middle; animation:blink 1s step-end infinite; margin-left:2px;}
  @keyframes blink{ 50%{ opacity:0; } }

  .hero-copy h1{
    font-family:var(--mono); font-weight:800; font-size:clamp(28px,4vw,40px);
    line-height:1.25; margin-bottom:16px;
  }
  .hero-copy h1 .accent{ color:var(--violet); }
  .hero-copy p{ color:var(--text-muted); font-size:16px; max-width:52ch; margin-bottom:26px;}
  .cta-row{ display:flex; gap:12px; flex-wrap:wrap; }
  .btn{
    font-family:var(--mono); font-size:13px; font-weight:600;
    padding:11px 18px; border-radius:8px; border:1px solid var(--border);
    display:inline-flex; align-items:center; gap:8px; transition:.2s;
  }
  .btn-primary{ background:var(--violet); color:#0d1117; border-color:var(--violet); }
  .btn-primary:hover{ background:var(--violet-dim); }
  .btn-ghost:hover{ border-color:var(--violet); color:var(--violet); }

  .avatar-card{
    background:var(--panel); border:1px solid var(--border); border-radius:var(--radius);
    padding:20px; text-align:center;
  }
  .avatar-card img{
    width:120px; height:120px; object-fit:cover; border-radius:50%;
    border:2px solid var(--g4); box-shadow:0 0 0 6px var(--violet-glow);
    margin-bottom:14px;
  }
  .avatar-card .status{ font-family:var(--mono); font-size:12px; color:var(--g4); display:flex; align-items:center; justify-content:center; gap:6px; margin-bottom:10px;}
  .avatar-card .status::before{ content:"●"; }
  .avatar-card h3{ font-size:16px; margin-bottom:2px; }
  .avatar-card p{ color:var(--text-muted); font-size:13px; }

  /* ---------- SECTION SHARED ---------- */
  section{ padding:64px 0; border-top:1px solid var(--border); }
  .sec-head{ display:flex; align-items:baseline; gap:12px; margin-bottom:32px; }
  .sec-head .tag{ font-family:var(--mono); font-size:12px; color:var(--g4); }
  .sec-head h2{ font-family:var(--mono); font-size:22px; font-weight:700; }

  /* ---------- ABOUT ---------- */
  .about-box{
    background:var(--panel); border:1px solid var(--border); border-radius:var(--radius);
    padding:26px 28px; position:relative; font-size:15.5px; color:#c9d1d9;
  }
  .about-box::before{ content:"/**"; display:block; font-family:var(--mono); color:var(--text-muted); margin-bottom:8px; }
  .about-box::after{ content:"*/"; display:block; font-family:var(--mono); color:var(--text-muted); margin-top:8px; }

  /* ---------- TIMELINE (git-log style) ---------- */
  .timeline{ position:relative; padding-left:28px; }
  .timeline::before{
    content:""; position:absolute; left:5px; top:6px; bottom:6px; width:2px;
    background:linear-gradient(var(--g4), var(--g2));
  }
  .commit{ position:relative; padding-bottom:36px; }
  .commit:last-child{ padding-bottom:0; }
  .commit::before{
    content:""; position:absolute; left:-28px; top:4px; width:12px; height:12px;
    border-radius:50%; background:var(--bg); border:2px solid var(--g4);
  }
  .commit.head::before{ background:var(--violet); border-color:var(--violet); box-shadow:0 0 0 4px var(--violet-glow); }
  .commit-head{ display:flex; align-items:center; gap:10px; flex-wrap:wrap; margin-bottom:6px; }
  .commit-head .badge{
    font-family:var(--mono); font-size:11px; background:var(--violet); color:#0d1117;
    padding:2px 8px; border-radius:20px; font-weight:700;
  }
  .commit-head .date{ font-family:var(--mono); font-size:12.5px; color:var(--text-muted); }
  .commit h3{ font-size:16px; margin-bottom:2px; }
  .commit .role{ font-family:var(--mono); font-size:13px; color:var(--g4); margin-bottom:8px; display:block;}
  .commit ul{ list-style:none; color:#c9d1d9; font-size:14.5px; }
  .commit li{ margin-bottom:6px; padding-left:16px; position:relative; }
  .commit li::before{ content:"+"; position:absolute; left:0; color:var(--g4); font-family:var(--mono); }

  /* ---------- PROJECTS ---------- */
  .projects-grid{ display:grid; grid-template-columns:1fr 1fr; gap:20px; }
  @media (max-width:700px){ .projects-grid{ grid-template-columns:1fr; } }
  .project-card{
    background:var(--panel); border:1px solid var(--border); border-radius:var(--radius);
    padding:22px; transition:.2s;
  }
  .project-card:hover{ border-color:var(--violet); transform:translateY(-3px); }
  .project-card h3{ font-size:16.5px; margin-bottom:10px; }
  .stack-row{ display:flex; flex-wrap:wrap; gap:6px; margin-bottom:14px; }
  .chip{
    font-family:var(--mono); font-size:11px; padding:3px 9px; border-radius:20px;
    border:1px solid var(--border); color:var(--text-muted);
  }
  .project-card ul{ list-style:none; font-size:14px; color:#c9d1d9;}
  .project-card li{ margin-bottom:6px; padding-left:14px; position:relative;}
  .project-card li::before{ content:"›"; position:absolute; left:0; color:var(--violet); }

  /* ---------- SKILLS ---------- */
  .skills-grid{ display:grid; grid-template-columns:repeat(2,1fr); gap:20px; }
  @media (max-width:700px){ .skills-grid{ grid-template-columns:1fr; } }
  .skill-group{ background:var(--panel); border:1px solid var(--border); border-radius:var(--radius); padding:18px 20px;}
  .skill-group h4{ font-family:var(--mono); font-size:12.5px; color:var(--g4); margin-bottom:12px; letter-spacing:.05em;}
  .skill-icons{ display:flex; flex-wrap:wrap; gap:10px; }
  .skill-pill{
    display:flex; align-items:center; gap:7px; font-size:13px;
    background:var(--bg-elev); border:1px solid var(--border); border-radius:8px; padding:6px 10px;
  }
  .skill-pill img{ width:16px; height:16px; }

  /* ---------- CONTRIBUTION STRIP (decorative signature) ---------- */
  .contrib{ display:flex; gap:3px; flex-wrap:wrap; margin-top:36px; opacity:.9; }
  .contrib span{ width:11px; height:11px; border-radius:2px; background:var(--border); }
  .contrib span.l1{ background:var(--g1); } .contrib span.l2{ background:var(--g2); }
  .contrib span.l3{ background:var(--g3); } .contrib span.l4{ background:var(--g4); }

  /* ---------- EDUCATION ---------- */
  .edu-card{
    background:var(--panel); border:1px solid var(--border); border-radius:var(--radius);
    padding:22px 24px; display:flex; align-items:center; gap:18px;
  }
  .edu-icon{
    width:44px; height:44px; border-radius:8px; background:var(--violet-glow);
    color:var(--violet); font-family:var(--mono); font-weight:800; font-size:16px;
    display:flex; align-items:center; justify-content:center; flex-shrink:0;
  }
  .edu-card h3{ font-size:15.5px; margin-bottom:2px; }
  .edu-card p{ font-size:13.5px; color:var(--text-muted); }

  /* ---------- FOOTER ---------- */
  footer{ padding:50px 0 60px; text-align:center; }
  footer .prompt-line{ font-family:var(--mono); font-size:14px; color:var(--text-muted); margin-bottom:20px; }
  footer .prompt-line .prompt{ color:var(--g4); }
  .foot-links{ display:flex; justify-content:center; gap:16px; flex-wrap:wrap; margin-bottom:24px; }
  .foot-links a{
    font-family:var(--mono); font-size:13px; padding:9px 16px; border:1px solid var(--border);
    border-radius:8px; transition:.2s;
  }
  .foot-links a:hover{ border-color:var(--violet); color:var(--violet); }
  footer .copyright{ font-family:var(--mono); font-size:12px; color:var(--text-muted); opacity:.7; }
</style>
</head>
<body>

<nav>
  <div class="wrap">
    <div class="brand"><span class="dot"></span> tandzp0o</div>
    <div class="navlinks">
      <a href="#about">about</a>
      <a href="#experience">experience</a>
      <a href="#projects">projects</a>
      <a href="#skills">skills</a>
      <a href="#contact">contact</a>
    </div>
  </div>
</nav>

<header class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <div class="eyebrow">AVAILABLE FOR OPPORTUNITIES</div>
      <div class="terminal" style="margin-bottom:26px;">
        <div class="terminal-bar">
          <span></span><span></span><span></span>
          <div class="terminal-title">tan@dev — zsh</div>
        </div>
        <div class="terminal-body">
          <div class="line"><span class="prompt">➜ ~</span> <span class="cmd">whoami</span></div>
          <span class="out-name">Lê Trương Trọng Tấn</span>
          <div class="out-title">Fullstack Developer · Next.js / Node.js / MongoDB</div>
          <div class="line" style="margin-top:14px;"><span class="prompt">➜ ~</span> <span class="cmd">cat focus.txt</span><span class="cursor"></span></div>
        </div>
      </div>
      <h1>Building ERP/CRM systems<br>that ship to <span class="accent">production</span>.</h1>
      <p>1+ year hands-on experience across the full stack — from requirement gathering with clients to deploying on Vercel. Currently completing a Master's in Information Technology, focused on AI/ML and algorithm optimization.</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="https://github.com/tandzp0o" target="_blank">↗ GitHub</a>
        <a class="btn btn-ghost" href="https://ltttan-portfolio.vercel.app/" target="_blank">Portfolio</a>
        <a class="btn btn-ghost" href="mailto:tannguyen0916@gmail.com">Email me</a>
      </div>
    </div>
    <div class="avatar-card">
      <img src="assets/avatar.jpg" alt="Lê Trương Trọng Tấn">
      <div class="status">open to work</div>
      <h3>Lê Trương Trọng Tấn</h3>
      <p>Tân Phú, HCM City</p>
      <p style="margin-top:8px;">📞 0916 467 039</p>
    </div>
  </div>
</header>

<section id="about">
  <div class="wrap">
    <div class="sec-head"><span class="tag">01</span><h2>about</h2></div>
    <div class="about-box">
      Software developer specializing in <strong>Next.js, React, Node.js and MongoDB</strong>, with a strong
      background in building and deploying ERP/CRM systems end-to-end — from requirement analysis through
      to production on Vercel. Currently pursuing a Master's degree in Information Technology with a focus
      on AI/ML models and algorithm optimization, and passionate about integrating AI into web applications.
    </div>
    <div class="contrib" aria-hidden="true">
      <span class="l2"></span><span class="l3"></span><span></span><span class="l4"></span><span class="l1"></span>
      <span class="l3"></span><span></span><span class="l4"></span><span class="l4"></span><span class="l2"></span>
      <span class="l1"></span><span></span><span class="l3"></span><span class="l4"></span><span class="l3"></span>
      <span class="l2"></span><span class="l4"></span><span></span><span class="l1"></span><span class="l3"></span>
      <span></span><span class="l4"></span><span class="l2"></span><span class="l3"></span><span></span>
      <span class="l1"></span><span class="l4"></span><span class="l4"></span><span class="l3"></span><span></span>
      <span class="l2"></span><span></span><span class="l4"></span><span class="l1"></span><span class="l3"></span>
      <span class="l4"></span><span></span><span class="l2"></span><span class="l3"></span><span class="l4"></span>
    </div>
  </div>
</section>

<section id="experience">
  <div class="wrap">
    <div class="sec-head"><span class="tag">02</span><h2>git log --experience</h2></div>
    <div class="timeline">
      <div class="commit head">
        <div class="commit-head"><span class="badge">HEAD</span><span class="date">Jan 2026 — Jul 2026</span></div>
        <h3>Wows</h3>
        <span class="role">R&amp;D</span>
        <ul>
          <li>Developed and deployed ERP/CRM modules using Next.js (App Router), Node.js and MongoDB, handling user workflows, forms and real-time data operations.</li>
          <li>Collaborated directly with clients on requirement gathering, training and troubleshooting — improving system usability.</li>
          <li>Integrated APIs and optimized database queries for better performance.</li>
        </ul>
      </div>
      <div class="commit">
        <div class="commit-head"><span class="date">Apr 2025 — Oct 2025</span></div>
        <h3>Mạng Xuyên Việt</h3>
        <span class="role">Developer</span>
        <ul>
          <li>Built and maintained ASP.NET WebForms applications, integrating frontend with backend and SQL Server.</li>
          <li>Implemented features based on client requirements, with a focus on performance optimization.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section id="projects">
  <div class="wrap">
    <div class="sec-head"><span class="tag">03</span><h2>projects</h2></div>
    <div class="projects-grid">
      <div class="project-card">
        <h3>ERP / Business Websites</h3>
        <div class="stack-row">
          <span class="chip">Next.js</span><span class="chip">Node.js</span><span class="chip">MongoDB</span>
          <span class="chip">ASP.NET WebForm</span><span class="chip">C#</span><span class="chip">SQL Server</span>
        </div>
        <ul>
          <li>Developed and maintained ERP/business website features.</li>
          <li>Implemented forms, workflows and database operations.</li>
        </ul>
      </div>
      <div class="project-card">
        <h3>Experimental Center Management System</h3>
        <div class="stack-row">
          <span class="chip">Next.js</span><span class="chip">React</span><span class="chip">TypeScript</span>
          <span class="chip">Node.js</span><span class="chip">PostgreSQL</span>
        </div>
        <ul>
          <li>Developed management features and responsive frontend interfaces.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section id="skills">
  <div class="wrap">
    <div class="sec-head"><span class="tag">04</span><h2>skills</h2></div>
    <div class="skills-grid">
      <div class="skill-group">
        <h4>FRONTEND</h4>
        <div class="skill-icons">
          <span class="skill-pill"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/react/react-original.svg" alt="">React.js</span>
          <span class="skill-pill"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/nextjs/nextjs-original.svg" alt="">Next.js</span>
          <span class="skill-pill"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/typescript/typescript-original.svg" alt="">TypeScript</span>
          <span class="skill-pill"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg" alt="">JavaScript</span>
          <span class="skill-pill"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/tailwindcss/tailwindcss-original.svg" alt="">TailwindCSS</span>
        </div>
      </div>
      <div class="skill-group">
        <h4>BACKEND</h4>
        <div class="skill-icons">
          <span class="skill-pill"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/nodejs/nodejs-original.svg" alt="">Node.js</span>
          <span class="skill-pill"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/dot-net/dot-net-original.svg" alt="">ASP.NET</span>
          <span class="skill-pill">⚙ RESTful APIs</span>
        </div>
      </div>
      <div class="skill-group">
        <h4>DATABASE</h4>
        <div class="skill-icons">
          <span class="skill-pill"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mongodb/mongodb-original.svg" alt="">MongoDB</span>
          <span class="skill-pill"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/microsoftsqlserver/microsoftsqlserver-plain.svg" alt="">SQL Server</span>
          <span class="skill-pill"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg" alt="">PostgreSQL</span>
        </div>
      </div>
      <div class="skill-group">
        <h4>TOOLS &amp; OTHERS</h4>
        <div class="skill-icons">
          <span class="skill-pill"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg" alt="">Git</span>
          <span class="skill-pill"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vercel/vercel-original.svg" alt="">Vercel</span>
          <span class="skill-pill">📮 Postman</span>
          <span class="skill-pill">🤖 AI-assisted dev</span>
          <span class="skill-pill">📋 Agile basics</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="education">
  <div class="wrap">
    <div class="sec-head"><span class="tag">05</span><h2>education</h2></div>
    <div class="edu-card">
      <div class="edu-icon">MS</div>
      <div>
        <h3>HCM City University of Industry and Trade</h3>
        <p>Master's Degree in Information Technology — currently completing thesis and final defense</p>
      </div>
    </div>
  </div>
</section>

<footer id="contact">
  <div class="wrap">
    <div class="prompt-line"><span class="prompt">➜ ~</span> git push origin let&#39;s-talk</div>
    <div class="foot-links">
      <a href="https://github.com/tandzp0o" target="_blank">GitHub ↗</a>
      <a href="https://ltttan-portfolio.vercel.app/" target="_blank">Portfolio ↗</a>
      <a href="https://www.facebook.com/trongtan.le.18" target="_blank">Facebook ↗</a>
      <a href="mailto:tannguyen0916@gmail.com">Email</a>
      <a href="tel:0916467039">0916 467 039</a>
    </div>
    <div class="copyright">© 2026 Lê Trương Trọng Tấn — built with Next.js energy, shipped as plain HTML.</div>
  </div>
</footer>

</body>
</html>
