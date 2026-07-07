<style>
  @import url('https://fonts.googleapis.com/css2?family=Readex+Pro:wght@300;400;500;600;700&display=swap');

  .profile-root {
    font-family: 'Readex Pro', system-ui, -apple-system, sans-serif;
    background: #000;
    color: #fff;
    -webkit-font-smoothing: antialiased;
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 4px 32px;
  }

  .profile-root a { color: rgba(255,255,255,0.85); }

  .section-card {
    background: rgba(23, 23, 23, 0.65);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 22px 26px;
    margin: 18px 0;
    text-align: left;
  }

  .section-title {
    font-weight: 500;
    letter-spacing: -0.02em;
    text-transform: lowercase;
    margin: 0 0 12px;
    font-size: 17px;
    color: #fff;
  }

  .section-card p {
    color: rgba(255, 255, 255, 0.82);
    font-size: 14px;
    line-height: 1.65;
    margin: 0;
  }

  .stats-row {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    justify-content: center;
    margin: 20px 0 8px;
  }

  .social-row {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    margin: 16px 0;
  }

  .social-row a {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(23, 23, 23, 0.9);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 999px;
    padding: 10px 18px;
    font-size: 12px;
    text-decoration: none;
    text-transform: lowercase;
    transition: background 0.2s ease, color 0.2s ease;
  }

  .social-row a:hover {
    background: rgba(38, 38, 38, 0.95);
    color: #fff;
  }

  .avatar-ring {
    border-radius: 50%;
    border: 2px solid rgba(255, 255, 255, 0.12);
    box-shadow: 0 0 0 6px rgba(255, 255, 255, 0.04);
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(18px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .fade-in { animation: fadeUp 0.7s ease forwards; }
  .fade-in-2 { animation: fadeUp 0.7s ease 0.12s forwards; opacity: 0; }
  .fade-in-3 { animation: fadeUp 0.7s ease 0.24s forwards; opacity: 0; }

  .exp-block {
    background: rgba(10, 10, 10, 0.8);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 16px 18px;
    font-family: ui-monospace, 'Cascadia Code', 'JetBrains Mono', monospace;
    font-size: 12px;
    line-height: 1.55;
    color: rgba(255,255,255,0.78);
    overflow-x: auto;
    white-space: pre;
    margin: 0;
  }
</style>

<div class="profile-root">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/hero.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/hero.svg">
  <img src="./assets/hero.svg" alt="build with purpose — fullstack developer" width="100%" />
</picture>

<div align="center" class="fade-in">

<img class="avatar-ring" src="assets/avatar.jpg" width="96" height="96" alt="Lê Trương Trọng Tấn" />

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Readex+Pro&weight=400&size=18&duration=2800&pause=1400&color=FFFFFF&center=true&vCenter=true&width=600&lines=fullstack+developer+%C2%B7+hcm+city;building+erp%2Fcrm+that+ship+to+production;next.js+%C2%B7+node.js+%C2%B7+mongodb;master%27s+in+ai%2Fml+in+progress)](https://github.com/tandzp0o)

</div>

<div class="social-row fade-in-2">
  <a href="https://github.com/tandzp0o">github</a>
  <a href="https://ltttan-portfolio.vercel.app/">portfolio</a>
  <a href="https://www.facebook.com/trongtan.le.18">facebook</a>
  <a href="mailto:tannguyen0916@gmail.com">email</a>
  <a href="tel:0916467039">phone</a>
</div>

<div class="stats-row fade-in-3">
  <img src="https://github-readme-stats.vercel.app/api?username=tandzp0o&show_icons=true&theme=dark&hide_border=true&bg_color=00000000&title_color=ffffff&text_color=a3a3a3&icon_color=ffffff&rank_icon=percentile" alt="github stats" height="165" />
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=tandzp0o&theme=dark&hide_border=true&background=00000000&ring=ffffff&fire=ffffff&currStreakLabel=ffffff&sideLabels=a3a3a3&dates=a3a3a3" alt="streak stats" height="165" />
</div>

<div class="stats-row">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=tandzp0o&layout=compact&theme=dark&hide_border=true&bg_color=00000000&title_color=ffffff&text_color=a3a3a3" alt="top languages" height="165" />
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=tandzp0o&theme=react-dark&hide_border=true&bg_color=000000&color=ffffff&line=ffffff&point=ffffff&area=true" alt="contribution graph" height="165" />
</div>

<div align="center">
  <img src="https://komarev.com/ghpvc/?username=tandzp0o&color=737373&style=flat-square&label=profile+views" alt="profile views" />
</div>

<br>

<div class="section-card" id="about">
  <p class="section-title">about</p>
  <p>software developer specializing in <strong>next.js, react, node.js and mongodb</strong>, with a strong background in building and deploying erp/crm systems end-to-end — from requirement analysis through to production on vercel. currently pursuing a master's degree in information technology with a focus on ai/ml models and algorithm optimization, and passionate about integrating ai into web applications.</p>
</div>

<div class="section-card" id="experience">
  <p class="section-title">git log --experience</p>
  <pre class="exp-block">* HEAD -> main   (Jan 2026 – Jul 2026)  Wows — R&amp;D
│   + Developed and deployed ERP/CRM modules using Next.js (App Router), Node.js, MongoDB
│   + Handled user workflows, forms and real-time data operations
│   + Collaborated with clients on requirement gathering, training and troubleshooting
│   + Integrated APIs and optimized database queries for performance
│
* (Apr 2025 – Oct 2025)  Mạng Xuyên Việt — Developer
    + Built and maintained ASP.NET WebForms applications
    + Integrated frontend with backend and SQL Server
    + Implemented features based on client requirements, with a focus on performance</pre>
</div>

</div>

### projects

| project | stack | highlights |
|---|---|---|
| **erp / business websites** | ![Next.js](https://img.shields.io/badge/-Next.js-000?logo=nextdotjs&logoColor=white) ![Node.js](https://img.shields.io/badge/-Node.js-339933?logo=nodedotjs&logoColor=white) ![MongoDB](https://img.shields.io/badge/-MongoDB-47A248?logo=mongodb&logoColor=white) ![.NET](https://img.shields.io/badge/-ASP.NET-512BD4?logo=dotnet&logoColor=white) | developed and maintained erp/business features; forms, workflows and database operations |
| **experimental center management** | ![Next.js](https://img.shields.io/badge/-Next.js-000?logo=nextdotjs&logoColor=white) ![React](https://img.shields.io/badge/-React-61DAFB?logo=react&logoColor=black) ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-4169E1?logo=postgresql&logoColor=white) | management features with responsive frontend interfaces |

<div class="profile-root">

<div class="section-card" id="skills">
  <p class="section-title">skills</p>
  <p>
    <strong>frontend</strong><br>
    <img src="https://img.shields.io/badge/-React.js-61DAFB?style=flat-square&logo=react&logoColor=black" alt="React" />
    <img src="https://img.shields.io/badge/-Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js" />
    <img src="https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
    <img src="https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript" />
    <img src="https://img.shields.io/badge/-TailwindCSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white" alt="Tailwind" />
    <br><br>
    <strong>backend</strong><br>
    <img src="https://img.shields.io/badge/-Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node.js" />
    <img src="https://img.shields.io/badge/-ASP.NET-512BD4?style=flat-square&logo=dotnet&logoColor=white" alt="ASP.NET" />
    <img src="https://img.shields.io/badge/-RESTful_APIs-25D366?style=flat-square&logo=fastapi&logoColor=white" alt="REST" />
    <br><br>
    <strong>database</strong><br>
    <img src="https://img.shields.io/badge/-MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white" alt="MongoDB" />
    <img src="https://img.shields.io/badge/-SQL_Server-CC2927?style=flat-square&logo=microsoftsqlserver&logoColor=white" alt="SQL Server" />
    <img src="https://img.shields.io/badge/-PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
    <br><br>
    <strong>tools</strong><br>
    <img src="https://img.shields.io/badge/-Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git" />
    <img src="https://img.shields.io/badge/-Vercel-000000?style=flat-square&logo=vercel&logoColor=white" alt="Vercel" />
    <img src="https://img.shields.io/badge/-Postman-FF6C37?style=flat-square&logo=postman&logoColor=white" alt="Postman" />
    <img src="https://img.shields.io/badge/-Agile-0052CC?style=flat-square&logo=jira&logoColor=white" alt="Agile" />
  </p>
</div>

<div class="section-card">
  <p class="section-title">education</p>
  <p><strong>hcm city university of industry and trade</strong> — master's degree in information technology <em>(currently completing thesis and final defense)</em></p>
</div>

</div>
