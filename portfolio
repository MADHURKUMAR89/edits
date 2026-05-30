<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>MASHER — Video Editor</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&family=DM+Serif+Display&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css" />
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg: #0c0c0c;
    --surface: #161616;
    --border: rgba(255,255,255,0.08);
    --border-md: rgba(255,255,255,0.15);
    --text: #f0ece4;
    --muted: #9a9590;
    --faint: #5a5650;
    --accent: #c8102e;
    --accent-bright: #e8192e;
    --tag-bg: #1e1e1e;
    --radius: 12px;
    --radius-sm: 8px;
    --font-display: 'DM Serif Display', serif;
    --font-body: 'DM Sans', sans-serif;
  }

  html { scroll-behavior: smooth; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: var(--font-body);
    font-size: 15px;
    line-height: 1.6;
  }

  body::before {
    content: '';
    position: fixed; inset: 0; z-index: 0;
    pointer-events: none;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
    background-size: 200px 200px;
    opacity: 0.35;
  }

  nav {
    position: sticky; top: 0; z-index: 100;
    display: flex; justify-content: space-between; align-items: center;
    padding: 1.1rem 2.5rem;
    background: rgba(12,12,12,0.90);
    backdrop-filter: blur(14px);
    border-bottom: 0.5px solid var(--border);
  }
  .logo {
    font-family: var(--font-display);
    font-size: 20px; letter-spacing: 4px;
    color: var(--text);
    text-decoration: none;
  }
  .logo span { color: var(--accent); }
  .nav-links { display: flex; gap: 2rem; list-style: none; }
  .nav-links a {
    font-size: 13px; color: var(--muted);
    text-decoration: none; letter-spacing: 0.4px;
    transition: color 0.2s;
  }
  .nav-links a:hover { color: var(--accent-bright); }

  .hero {
    padding: 6rem 2.5rem 5rem;
    max-width: 860px;
    animation: fadeUp 0.7s ease both;
    position: relative; z-index: 1;
  }
  .hero-eyebrow {
    display: inline-flex; align-items: center; gap: 8px;
    font-size: 11px; letter-spacing: 2.5px; color: var(--muted);
    text-transform: uppercase; margin-bottom: 1.4rem;
  }
  .dot {
    width: 6px; height: 6px; border-radius: 50%;
    background: var(--accent);
    display: inline-block;
    box-shadow: 0 0 8px var(--accent);
    animation: pulse 2s ease-in-out infinite;
  }
  @keyframes pulse {
    0%, 100% { box-shadow: 0 0 6px var(--accent); }
    50% { box-shadow: 0 0 14px var(--accent-bright); }
  }
  .hero h1 {
    font-family: var(--font-display);
    font-size: clamp(38px, 6vw, 60px);
    font-weight: 400; line-height: 1.1;
    color: var(--text); margin-bottom: 1.4rem;
  }
  .hero h1 em { color: var(--accent); font-style: italic; }
  .hero p {
    font-size: 16px; color: var(--muted);
    max-width: 620px; margin-bottom: 2.2rem; line-height: 1.85;
  }
  .btn-row { display: flex; gap: 12px; flex-wrap: wrap; }
  .btn-dark {
    padding: 11px 24px; font-size: 13px; font-weight: 500;
    background: var(--accent); color: #fff;
    border: none; border-radius: 100px; cursor: pointer;
    font-family: var(--font-body); letter-spacing: 0.3px;
    text-decoration: none; display: inline-block;
    transition: background 0.2s, box-shadow 0.2s;
    box-shadow: 0 0 18px rgba(200,16,46,0.35);
  }
  .btn-dark:hover { background: var(--accent-bright); box-shadow: 0 0 28px rgba(232,25,46,0.5); }
  .btn-light {
    padding: 11px 24px; font-size: 13px; font-weight: 500;
    background: transparent; color: var(--text);
    border: 0.5px solid var(--border-md); border-radius: 100px;
    cursor: pointer; font-family: var(--font-body);
    text-decoration: none; display: inline-block;
    transition: background 0.2s, border-color 0.2s;
  }
  .btn-light:hover { background: rgba(255,255,255,0.05); border-color: var(--accent); }

  .divider { border: none; border-top: 0.5px solid var(--border); margin: 0 2.5rem; position: relative; z-index: 1; }

  .section { padding: 3rem 2.5rem; position: relative; z-index: 1; }
  .section-label {
    font-size: 11px; letter-spacing: 2.5px; color: var(--accent);
    text-transform: uppercase; margin-bottom: 1.4rem;
    opacity: 0.8;
  }

  .tags { display: flex; gap: 8px; flex-wrap: wrap; }
  .tag {
    font-size: 13px; padding: 6px 16px;
    background: var(--tag-bg);
    border: 0.5px solid var(--border);
    border-radius: 100px;
    color: var(--muted); display: flex; align-items: center; gap: 6px;
    transition: border-color 0.2s, color 0.2s;
  }
  .tag:hover { border-color: var(--accent); color: var(--text); }
  .tag i { font-size: 14px; }

  .works-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 14px;
  }
  .work-card {
    background: var(--surface);
    border: 0.5px solid var(--border);
    border-radius: var(--radius);
    overflow: hidden;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
    text-decoration: none; color: inherit;
    display: block;
  }
  .work-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 32px rgba(200,16,46,0.15);
    border-color: rgba(200,16,46,0.35);
  }
  .work-thumb {
    height: 130px; display: flex; align-items: center; justify-content: center;
    position: relative; overflow: hidden;
  }
  .thumb-youtube { background: #1c1010; }
  .thumb-wedding { background: #121218; }
  .thumb-reel    { background: #101218; }
  .thumb-event   { background: #181012; }
  .work-thumb i { font-size: 36px; color: rgba(200,16,46,0.35); transition: color 0.2s; }
  .work-card:hover .work-thumb i { color: var(--accent-bright); }
  .ext-badge {
    position: absolute; top: 10px; right: 10px;
    background: var(--accent); color: #fff;
    font-size: 10px; letter-spacing: 1px; padding: 3px 8px;
    border-radius: 4px; text-transform: uppercase;
  }
  .work-info { padding: 14px 16px; }
  .work-title { font-size: 13px; font-weight: 500; color: var(--text); margin-bottom: 4px; }
  .work-meta { font-size: 11px; color: var(--faint); letter-spacing: 0.4px; }

  .reel-block {
    background: var(--surface);
    border: 0.5px solid var(--border);
    border-radius: var(--radius);
    padding: 3rem 2rem; text-align: center;
    position: relative; overflow: hidden;
  }
  .reel-block::before {
    content: '';
    position: absolute; inset: 0;
    background: radial-gradient(ellipse at 50% 50%, rgba(200,16,46,0.08) 0%, transparent 70%);
    pointer-events: none;
  }
  .play-btn {
    width: 60px; height: 60px; border-radius: 50%;
    background: var(--accent);
    display: flex; align-items: center; justify-content: center;
    margin: 0 auto 1.2rem; cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
    border: none;
    text-decoration: none;
    box-shadow: 0 0 24px rgba(200,16,46,0.45);
  }
  .play-btn:hover { transform: scale(1.1); box-shadow: 0 0 36px rgba(232,25,46,0.65); }
  .play-btn i { font-size: 22px; color: #fff; margin-left: 3px; }
  .reel-title { font-size: 16px; font-weight: 500; margin-bottom: 6px; color: var(--text); }
  .reel-sub { font-size: 13px; color: var(--muted); }

  .tools-row { display: flex; gap: 8px; flex-wrap: wrap; }
  .tool-chip {
    font-size: 12px; padding: 6px 14px;
    background: var(--surface);
    border: 0.5px solid var(--border);
    border-radius: var(--radius-sm);
    color: var(--muted);
    transition: border-color 0.2s, color 0.2s;
  }
  .tool-chip:hover { border-color: var(--accent); color: var(--text); }

  .contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }
  @media (max-width: 600px) { .contact-grid { grid-template-columns: 1fr; } }
  .contact-info h3 {
    font-family: var(--font-display);
    font-size: 26px; font-weight: 400;
    margin-bottom: 0.8rem; color: var(--text);
  }
  .contact-info p { font-size: 14px; color: var(--muted); line-height: 1.75; margin-bottom: 1.2rem; }
  .contact-detail { display: flex; align-items: center; gap: 8px; font-size: 13px; color: var(--muted); margin-bottom: 8px; }
  .contact-detail i { font-size: 16px; color: var(--accent); }

  .contact-form { display: flex; flex-direction: column; gap: 10px; }
  .contact-form input,
  .contact-form textarea {
    width: 100%; padding: 10px 14px; font-size: 13px;
    border: 0.5px solid var(--border-md);
    border-radius: var(--radius-sm);
    background: var(--surface); color: var(--text);
    font-family: var(--font-body);
    outline: none; transition: border-color 0.2s;
  }
  .contact-form input::placeholder,
  .contact-form textarea::placeholder { color: var(--faint); }
  .contact-form input:focus,
  .contact-form textarea:focus { border-color: var(--accent); }
  .contact-form textarea { resize: vertical; min-height: 90px; }

  footer {
    padding: 1.5rem 2.5rem;
    border-top: 0.5px solid var(--border);
    display: flex; justify-content: space-between; align-items: center;
    flex-wrap: wrap; gap: 12px;
    position: relative; z-index: 1;
  }
  footer span { font-size: 12px; color: var(--faint); }
  .social-row { display: flex; gap: 16px; }
  .social-row a { font-size: 20px; color: var(--faint); text-decoration: none; transition: color 0.2s; }
  .social-row a:hover { color: var(--accent-bright); }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
  }
</style>
</head>
<body>

<nav>
  <a href="#" class="logo">MAS<span>H</span>ER</a>
  <ul class="nav-links">
    <li><a href="#work">Work</a></li>
    <li><a href="#reel">Reel</a></li>
    <li><a href="#about">About</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
</nav>

<section class="hero">
  <div class="hero-eyebrow">
    <span class="dot"></span>
    Available for projects · Based in India
  </div>
  <h1>Crafting stories,<br><em>frame by frame.</em></h1>
  <p>I transform raw footage into cinematic stories that connect with people emotionally. Through precise editing, sound design, and color grading, I bring life, rhythm, and feeling to every vlog and reel. My goal is simple — to create visuals that people don't just watch, but truly experience.</p>
  <div class="btn-row">
    <a href="#contact" class="btn-dark">Work with me</a>
  </div>
</section>

<hr class="divider" />

<section class="section" id="about">
  <p class="section-label">Specialties</p>
  <div class="tags">
    <span class="tag"><i class="ti ti-device-tv"></i> YouTube &amp; Vlogs</span>
    <span class="tag"><i class="ti ti-device-mobile"></i> Social Media Reels</span>
    <span class="tag"><i class="ti ti-heart"></i> Weddings &amp; Events</span>
    <span class="tag"><i class="ti ti-color-swatch"></i> Color Grading</span>
    <span class="tag"><i class="ti ti-music"></i> Sound Design</span>
    <span class="tag"><i class="ti ti-cut"></i> Motion Editing</span>
  </div>
</section>

<hr class="divider" />

<section class="section" id="work">
  <p class="section-label">Selected work</p>
  <div class="works-grid">

    <a class="work-card" href="https://youtu.be/5bNp0VifFq4?si=IA6nVr3rOyP4SdM5" target="_blank" rel="noopener">
      <div class="work-thumb thumb-youtube">
        <i class="ti ti-brand-youtube"></i>
        <span class="ext-badge">YouTube</span>
      </div>
      <div class="work-info">
        <p class="work-title">YouTube Travel Vlog</p>
        <p class="work-meta">YOUTUBE · VLOG</p>
      </div>
    </a>

    <a class="work-card" href="https://www.instagram.com/reel/DXvOVCGJ8US/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==" target="_blank" rel="noopener">
      <div class="work-thumb thumb-reel">
        <i class="ti ti-brand-instagram"></i>
        <span class="ext-badge">Reel</span>
      </div>
      <div class="work-info">
        <p class="work-title">Brand Instagram Reel</p>
        <p class="work-meta">SOCIAL MEDIA · 30 SEC</p>
      </div>
    </a>

    <div class="work-card">
      <div class="work-thumb thumb-wedding">
        <i class="ti ti-heart"></i>
      </div>
      <div class="work-info">
        <p class="work-title">Wedding Highlight Film</p>
        <p class="work-meta">WEDDING · 4 MIN</p>
      </div>
    </div>

    <div class="work-card">
      <div class="work-thumb thumb-event">
        <i class="ti ti-confetti"></i>
      </div>
      <div class="work-info">
        <p class="work-title">Birthday Event Film</p>
        <p class="work-meta">EVENT · 6 MIN</p>
      </div>
    </div>

  </div>
</section>

<hr class="divider" />

<!-- SHOWREEL — updated to Instagram reel -->
<section class="section" id="reel">
  <p class="section-label">Showreel</p>
  <div class="reel-block">
    <a class="play-btn" href="https://www.instagram.com/reel/DWeEv7cjKpf/?igsh=eHFpdTRwdmpreDNt" target="_blank" rel="noopener" aria-label="Play showreel">
      <i class="ti ti-player-play"></i>
    </a>
    <p class="reel-title">Masher — 2024 Showreel</p>
    <p class="reel-sub">A highlight of my best work across weddings, YouTube &amp; reels.</p>
  </div>
</section>

<hr class="divider" />

<section class="section">
  <p class="section-label">Tools &amp; software</p>
  <div class="tools-row">
    <span class="tool-chip">Adobe Premiere Pro</span>
    <span class="tool-chip">DaVinci Resolve</span>
    <span class="tool-chip">After Effects</span>
    <span class="tool-chip">Adobe Audition</span>
    <span class="tool-chip">Lightroom</span>
  </div>
</section>

<hr class="divider" />

<section class="section" id="contact">
  <p class="section-label">Get in touch</p>
  <div class="contact-grid">
    <div class="contact-info">
      <h3>Let's work<br>together.</h3>
      <p>Have a project in mind? Drop a message and I'll get back to you within 24 hours.</p>
      <div class="contact-detail"><i class="ti ti-map-pin"></i> India</div>
      <div class="contact-detail"><i class="ti ti-mail"></i> <a href="mailto:madhurkumar8989@gmail.com" style="color:var(--muted);text-decoration:none;">madhurkumar8989@gmail.com</a></div>
      <div class="contact-detail"><i class="ti ti-clock"></i> Response within 24 hrs</div>
    </div>
    <form class="contact-form" id="contactForm">
      <input type="text" id="from_name" placeholder="Your name" required />
      <input type="email" id="from_email" placeholder="Your email" required />
      <textarea id="message" placeholder="Tell me about your project…" required></textarea>
      <button type="submit" id="submitBtn" class="btn-dark" style="border-radius: 8px; padding: 11px; font-size: 13px;">Send message</button>
      <p id="formStatus" style="font-size:13px; text-align:center; display:none;"></p>
    </form>
  </div>
</section>

<footer>
  <span>© 2024 Masher. All rights reserved.</span>
  <div class="social-row">
    <a href="mailto:madhurkumar8989@gmail.com" aria-label="Email"><i class="ti ti-mail"></i></a>
    <a href="https://www.instagram.com/madhur_saini__432?igsh=MXAzZGI5bXdwaDFmYg==" target="_blank" aria-label="Instagram"><i class="ti ti-brand-instagram"></i></a>
  </div>
</footer>

<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
<script>
  emailjs.init('0HXEuiV0pbDGfqYux');

  document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const btn = document.getElementById('submitBtn');
    const status = document.getElementById('formStatus');
    btn.textContent = 'Sending…';
    btn.disabled = true;

    const params = {
      from_name: document.getElementById('from_name').value,
      from_email: document.getElementById('from_email').value,
      message: document.getElementById('message').value,
      to_email: 'madhurkumar8989@gmail.com'
    };

    emailjs.send('service_avvuf52', 'template_p3cc1sb', params)
      .then(function() {
        status.textContent = '✓ Message sent! I\'ll get back to you within 24 hours.';
        status.style.color = '#e8192e';
        status.style.display = 'block';
        btn.textContent = 'Sent!';
        document.getElementById('contactForm').reset();
      }, function(error) {
        status.textContent = 'Something went wrong. Please email me directly at madhurkumar8989@gmail.com';
        status.style.color = '#e05c5c';
        status.style.display = 'block';
        btn.textContent = 'Send message';
        btn.disabled = false;
      });
  });
</script>

</body>
</html>
