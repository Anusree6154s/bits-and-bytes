---
permalink: /about
layout: default
title: About Me
nav_order: 2
---

<div class="scratchpad-container">
  
  <div class="sticky-note yellow-note">
    <div class="pin">📍</div>
    <div class="note-title">Hey there! 👋</div>
    <p class="note-body">
      This site is my personal documentation, made public for anyone who might find my code scribbles useful.
    </p>
  </div>

  <div class="sticky-note blue-note">
    <div class="pin">📍</div>
    <div class="note-title">Who Am I? </div>
    <p class="note-body">
      <strong>Full Stack Developer</strong> diving into the <strong>MERN stack</strong> (React, Redux, Express, MongoDB) with some Next.js and TypeScript on the side.
    </p>
  </div>

  <div class="sticky-note pink-note">
    <div class="pin">📍</div>
    <div class="note-title">Why This Site?</div>
    <p class="note-body">
      To jot down anything that I find difficult in my tech journey.
    </p>
  </div>

  <div class="sticky-note green-note full-width">
    <div class="pin">📍</div>
    <div class="note-title">Fun Facts </div>
    <ul class="note-list">
      <li>Love cat memes, mystery series, and animated movies.</li>
      <li>While I’m reserved, I communicate best through text.</li>
      <li>Enjoys solving problems and contributing to open-source..</li>
    </ul>
  </div>

</div>
<br>



<style>
.scratchpad-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.25rem;
  margin: 2rem 0;
}

.sticky-note {
  position: relative;
  padding: 1.25rem;
  border-radius: 2px;
  box-shadow: 2px 4px 10px rgba(0,0,0,0.06);
  transition: transform 0.2s ease;
}



.yellow-note { background: #fef08a; color: #713f12; transform: rotate(-1deg); }
.blue-note   { background: #e0f2fe; color: #0369a1; transform: rotate(1.5deg); }
.pink-note   { background: #fce7f3; color: #be185d; transform: rotate(-1.5deg); }
.green-note  { background: #dcfce7; color: #15803d; transform: rotate(1deg); }

.full-width { grid-column: 1 / -1; }
.three-quarter-width {grid-column: span 3;}
.quarter-width { grid-column: span 1;}

.pin {
  position: absolute;
  top: -8px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 0.85rem;
}

.note-title {
  font-weight: 700;
  font-size: 1rem;
  margin-bottom: 0.5rem;
}

.note-body {
  font-size: 0.88rem;
  line-height: 1.5;
  margin: 0;
}

.note-list {
  margin: 0;
  padding-left: 1.1rem;
  font-size: 0.88rem;
  line-height: 1.6;
}

.connect-paper {
  background: #f8fafc;
  border: 1px dashed #cbd5e1;
  padding: 1rem;
  border-radius: 8px;
  display: flex;
  gap: 1rem;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  font-size: 0.9rem;
  color: #475569;
}

.connect-paper a {
  color: #0f172a;
  font-weight: 600;
  text-decoration: underline;
}
</style>
<div class="stitched-connect">
  <span class="stitched-label">Connect with me at:</span>
  <div class="stitched-links">
    <a href="https://github.com/Anusree6154s" target="_blank">GitHub</a>
    <a href="https://x.com/anu6154s" target="_blank">Twitter</a>
    <a href="https://www.linkedin.com/in/anusreeanilkumar1/" target="_blank">LinkedIn</a>
  </div>
</div>

<style>
.stitched-connect {
  border-top: 1.5px dashed #cbd5e1;
  padding-top: 1rem;
  margin-top: 1rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.85rem;
  color: #64748b;
}

.stitched-label {
  font-weight: 600;
}

.stitched-links {
  display: flex;
  gap: 1.25rem;
}

.stitched-links a {
  color: #1e293b;
  font-weight: 600;
  text-decoration: none;
  position: relative;
}

.stitched-links a:hover {
  text-decoration: underline;
  color: #0284c7;
}
</style>