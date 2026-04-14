
# Run this script once to generate the new interactive-lab.html
# python write_new_lab.py

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Interactive Lab - Dr. Junaid Qadir</title>
    <link rel="stylesheet" href="styles.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
    <style>
        body.interactive-lab { background: #050d1a; }
        .lab-intro { text-align:center; padding:18px 20px 6px; color:#a0c4ff; font-size:1.05rem; }
        .lab-tabs { display:flex; flex-wrap:wrap; justify-content:center; gap:10px; margin:18px auto 28px; max-width:1100px; }
        .lab-tab-btn { background:rgba(255,255,255,0.07); border:1.5px solid #4fc3f7; color:#4fc3f7; border-radius:30px; padding:9px 20px; font-size:0.9rem; font-weight:600; cursor:pointer; transition:all 0.2s; }
        .lab-tab-btn:hover,.lab-tab-btn.active { background:#4fc3f7; color:#000; }
        .lab-panel { display:none; max-width:960px; margin:0 auto 40px; }
        .lab-panel.active { display:block; }
        .lab-card { background:rgba(255,255,255,0.05); border:1px solid rgba(79,195,247,0.25); border-radius:14px; padding:28px 32px; margin-bottom:22px; }
        .lab-card h2 { color:#4fc3f7; margin-top:0; font-size:1.35rem; border-bottom:1px solid rgba(79,195,247,0.2); padding-bottom:10px; margin-bottom:18px; }
        .quiz-question { font-size:1.1rem; font-weight:600; margin-bottom:14px; color:#e0e0e0; }
        .quiz-options { display:flex; flex-direction:column; gap:10px; }
        .quiz-opt { background:rgba(255,255,255,0.07); border:1.5px solid rgba(79,195,247,0.3); border-radius:8px; padding:11px 16px; cursor:pointer; color:#ccc; font-size:0.97rem; transition:all 0.2s; text-align:left; }
        .quiz-opt:hover:not(:disabled) { border-color:#4fc3f7; color:#fff; }
        .quiz-opt.correct { background:rgba(76,175,80,0.25); border-color:#4caf50; color:#a5d6a7; }
        .quiz-opt.wrong { background:rgba(244,67,54,0.2); border-color:#f44336; color:#ef9a9a; }
        .quiz-feedback { margin-top:14px; font-size:0.95rem; min-height:22px; line-height:1.5; color:#ccc; }
        .quiz-nav { display:flex; gap:12px; margin-top:18px; align-items:center; flex-wrap:wrap; }
        .quiz-nav button { background:#4fc3f7; color:#000; border:none; border-radius:8px; padding:9px 22px; font-weight:700; cursor:pointer; font-size:0.95rem; }
        .quiz-streak { font-size:0.9rem; color:#ffcc02; margin-left:auto; }
        .quiz-progress-bar { height:6px; background:rgba(79,195,247,0.15); border-radius:3px; margin-bottom:14px; }
        .quiz-progress-fill { height:100%; background:#4fc3f7; border-radius:3px; transition:width 0.4s; }
        .quiz-meta { display:flex; justify-content:space-between; font-size:0.82rem; color:#888; margin-bottom:10px; }
        .quiz-loading { text-align:center; padding:40px; color:#a0c4ff; font-size:1.05rem; }
        .quiz-loading .spinner { display:inline-block; width:28px; height:28px; border:3px solid rgba(79,195,247,0.2); border-top-color:#4fc3f7; border-radius:50%; animation:spin 0.8s linear infinite; margin-bottom:12px; }
        @keyframes spin { to { transform:rotate(360deg); } }
        .quiz-topic-bar { display:flex; flex-wrap:wrap; gap:8px; margin-bottom:18px; }
        .quiz-topic-btn { background:rgba(255,255,255,0.05); border:1px solid rgba(79,195,247,0.3); color:#a0c4ff; border-radius:20px; padding:5px 14px; font-size:0.82rem; cursor:pointer; transition:all 0.15s; }
        .quiz-topic-btn:hover,.quiz-topic-btn.active { background:rgba(79,195,247,0.2); border-color:#4fc3f7; color:#fff; }
        .sig-controls { display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:18px; margin-bottom:22px; }
        .sig-control label { display:block; color:#a0c4ff; font-size:0.88rem; margin-bottom:5px; font-weight:600; }
        .sig-control input[type=range] { width:100%; accent-color:#4fc3f7; }
        .sig-control .val { color:#4fc3f7; font-weight:700; }
        #sig-canvas { width:100%; border-radius:10px; background:#050d1a; border:1px solid rgba(79,195,247,0.2); }
        .sig-info { display:flex; gap:14px; flex-wrap:wrap; margin-top:14px; }
        .sig-info-item { background:rgba(79,195,247,0.08); border-radius:8px; padding:10px 16px; }
        .sig-info-item .label { font-size:0.76rem; color:#888; }
        .sig-info-item .value { font-size:1.05rem; color:#4fc3f7; font-weight:700; }
        .sig-legend { display:flex; gap:18px; margin-bottom:12px; flex-wrap:wrap; }
        .sig-legend-item { display:flex; align-items:center; gap:7px; font-size:0.88rem; color:#ccc; }
        .sig-legend-dot { width:14px; height:4px; border-radius:2px; }
        .attack-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:12px; margin-bottom:18px; }
        .attack-card { background:rgba(255,255,255,0.04); border:1.5px solid rgba(79,195,247,0.2); border-radius:10px; padding:14px; cursor:pointer; transition:all 0.2s; }
        .attack-card:hover { border-color:#f44336; background:rgba(244,67,54,0.07); }
        .attack-card.selected { border-color:#f44336; background:rgba(244,67,54,0.12); }
        .attack-card h4 { color:#ef9a9a; margin:0 0 5px; font-size:0.95rem; }
        .attack-card p { color:#999; font-size:0.82rem; margin:0; }
        #attack-canvas { width:100%; border-radius:10px; background:#050d1a; border:1px solid rgba(79,195,247,0.2); margin-bottom:14px; }
        .attack-info { background:rgba(244,67,54,0.08); border:1px solid rgba(244,67,54,0.3); border-radius:10px; padding:16px 20px; display:none; }
        .attack-info.visible { display:block; }
        .attack-info h4 { color:#ef9a9a; margin:0 0 8px; }
        .attack-info p { color:#ccc; font-size:0.92rem; margin:0 0 6px; }
        .attack-info .countermeasure { color:#a5d6a7; font-size:0.9rem; }
        #nn-canvas { width:100%; border-radius:10px; background:#050d1a; border:1px solid rgba(79,195,247,0.2); }
        .nn-controls { display:flex; flex-wrap:wrap; gap:14px; margin-bottom:18px; align-items:flex-end; }
        .nn-controls label { color:#a0c4ff; font-size:0.88rem; font-weight:600; display:block; margin-bottom:4px; }
        .nn-controls input[type=range] { accent-color:#4fc3f7; width:120px; display:block; }
        .nn-controls .val { color:#4fc3f7; font-weight:700; }
        .nn-controls button { background:#4fc3f7; color:#000; border:none; border-radius:8px; padding:8px 20px; font-weight:700; cursor:pointer; font-size:0.9rem; }
        .nn-info { margin-top:14px; display:flex; gap:14px; flex-wrap:wrap; }
        .nn-info-item { background:rgba(79,195,247,0.08); border-radius:8px; padding:10px 16px; }
        .nn-info-item .label { font-size:0.76rem; color:#888; }
        .nn-info-item .value { font-size:1.05rem; color:#4fc3f7; font-weight:700; }
        #robot-canvas { width:100%; border-radius:10px; background:#050d1a; border:1px solid rgba(79,195,247,0.2); cursor:pointer; }
        .robot-controls { display:flex; flex-wrap:wrap; gap:10px; margin-bottom:16px; }
        .robot-controls button { background:rgba(79,195,247,0.12); border:1.5px solid #4fc3f7; color:#4fc3f7; border-radius:8px; padding:8px 16px; font-weight:600; cursor:pointer; font-size:0.85rem; transition:all 0.2s; }
        .robot-controls button:hover { background:#4fc3f7; color:#000; }
        .robot-controls button.danger { border-color:#f44336; color:#f44336; }
        .robot-controls button.danger:hover { background:#f44336; color:#fff; }
        .robot-status { background:rgba(0,0,0,0.3); border-radius:8px; padding:10px 16px; font-size:0.88rem; color:#a0c4ff; margin-bottom:14px; min-height:38px; }
        .robot-legend { display:flex; flex-wrap:wrap; gap:14px; margin-top:12px; }
        .robot-legend-item { display:flex; align-items:center; gap:6px; font-size:0.82rem; color:#ccc; }
        .robot-legend-dot { width:12px; height:12px; border-radius:3px; }
        .ttt-controls { display:flex; gap:20px; font-weight:600; margin-bottom:16px; flex-wrap:wrap; }
        .ttt-controls label { color:#ccc; cursor:pointer; display:flex; align-items:center; gap:6px; }
        #ttt-board { display:grid; grid-template-columns:repeat(3,90px); gap:8px; justify-content:center; margin:16px auto; }
        .ttt-cell { width:90px; height:90px; background:rgba(255,255,255,0.08); border:2px solid rgba(79,195,247,0.4); border-radius:10px; font-size:2.4rem; font-weight:bold; color:#4fc3f7; display:flex; align-items:center; justify-content:center; cursor:pointer; user-select:none; transition:all 0.15s; }
        .ttt-cell:hover:not(.taken) { background:rgba(79,195,247,0.15); }
        .ttt-cell.taken { cursor:default; }
        .ttt-cell.o-cell { color:#f48fb1; }
        .ttt-cell.win-cell { background:rgba(79,195,247,0.2); border-color:#4fc3f7; }
        #ttt-status { text-align:center; font-weight:700; font-size:1.05rem; color:#a0c4ff; margin:8px 0; }
        #ttt-reset { display:block; margin:12px auto 0; background:#4fc3f7; color:#000; border:none; border-radius:8px; padding:9px 28px; font-weight:700; cursor:pointer; font-size:0.95rem; }
        .ttt-score-board { display:flex; justify-content:center; gap:30px; margin-bottom:12px; flex-wrap:wrap; }
        .ttt-score-item { text-align:center; }
        .ttt-score-item .s-label { font-size:0.78rem; color:#888; }
        .ttt-score-item .s-value { font-size:1.5rem; font-weight:700; color:#4fc3f7; }
        .ttt-score-item.o-score .s-value { color:#f48fb1; }
    </style>
</head>
<body class="interactive-lab">
    <div class="hero-content">
        <header class="hero">
            <img src="profile.jpg" alt="Dr. Junaid Qadir" class="profile-photo" />
            <h1>Junaid Qadir <span style="font-size:0.6em; font-style:italic;">(Ph.D.)</span></h1>
            <p>Postdoctoral Researcher</p>
            <p>Department of Computer Science, School of Science and Technology</p>
            <p>Örebro University, Sweden</p>
        </header>
    </div>
    <div class="page-content">
        <aside class="topbar">
            <nav>
                <a href="index.html">Home</a>
                <a href="education.html">Education</a>
                <a href="research.html">Research</a>
                <a href="experience.html">Experience</a>
                <a href="publications.html">Publications</a>
                <a href="projects.html">Projects</a>
                <a href="activities.html">Professional Activities</a>
                <a href="contact.html">Contact</a>
                <a href="interactive-lab.html" class="active">Interactive Lab</a>
            </nav>
        </aside>
        <main>
            <p class="lab-intro">Welcome to the Interactive Lab — explore cybersecurity, AI, robotics and signal processing through hands-on demos inspired by real research!</p>
            <div class="lab-tabs">
                <button class="lab-tab-btn active" onclick="showTab('quiz',this)">🔐 AI Quiz</button>
                <button class="lab-tab-btn" onclick="showTab('signal',this)">📡 Signal Visualizer</button>
                <button class="lab-tab-btn" onclick="showTab('attack',this)">⚠️ Attack Simulator</button>
                <button class="lab-tab-btn" onclick="showTab('nn',this)">🧠 Neural Network</button>
                <button class="lab-tab-btn" onclick="showTab('robot',this)">🤖 Robot Navigator</button>
                <button class="lab-tab-btn" onclick="showTab('ttt',this)">🎮 Tic Tac Toe</button>
            </div>
            <div id="panel-quiz" class="lab-panel active">
                <div class="lab-card">
                    <h2>🔐 Unlimited AI-Powered Cybersecurity Quiz</h2>
                    <p style="color:#999;font-size:0.9rem;margin-bottom:14px;">Questions generated live by AI — endless unique questions. Pick a topic and go!</p>
                    <div class="quiz-topic-bar" id="quiz-topics"></div>
                    <div id="quiz-container"><div class="quiz-loading"><div class="spinner"></div><br>Loading your first question...</div></div>
                </div>
            </div>
            <div id="panel-signal" class="lab-panel">
                <div class="lab-card">
                    <h2>📡 IMU Signal and Noise Visualizer</h2>
                    <p style="color:#999;font-size:0.92rem;margin-bottom:18px;">Adjust sliders to see how frequency and noise affect a sensor signal — just like IMU data used in postural balance research.</p>
                    <div class="sig-controls">
                        <div class="sig-control"><label>Frequency: <span class="val" id="freq-val">2 Hz</span></label><input type="range" id="sig-freq" min="1" max="10" value="2" step="0.5"></div>
                        <div class="sig-control"><label>Amplitude: <span class="val" id="amp-val">1.0</span></label><input type="range" id="sig-amp" min="0.2" max="3" value="1" step="0.1"></div>
                        <div class="sig-control"><label>Noise Level: <span class="val" id="noise-val">0.1</span></label><input type="range" id="sig-noise" min="0" max="2" value="0.1" step="0.05"></div>
                        <div class="sig-control"><label>2nd Component: <span class="val" id="comp2-val">Off</span></label><input type="range" id="sig-comp2" min="0" max="3" value="0" step="0.5"></div>
                    </div>
                    <div class="sig-legend">
                        <div class="sig-legend-item"><div class="sig-legend-dot" style="background:#4fc3f7"></div>Clean Signal</div>
                        <div class="sig-legend-item"><div class="sig-legend-dot" style="background:#f48fb1"></div>Noisy Signal</div>
                    </div>
                    <canvas id="sig-canvas" height="220"></canvas>
                    <div class="sig-info">
                        <div class="sig-info-item"><div class="label">SNR</div><div class="value" id="snr-val">—</div></div>
                        <div class="sig-info-item"><div class="label">Peak Amplitude</div><div class="value" id="peak-val">—</div></div>
                        <div class="sig-info-item"><div class="label">Signal Quality</div><div class="value" id="quality-val">—</div></div>
                    </div>
                </div>
            </div>
            <div id="panel-attack" class="lab-panel">
                <div class="lab-card">
                    <h2>⚠️ LoRaWAN Network Attack Simulator</h2>
                    <p style="color:#999;font-size:0.92rem;margin-bottom:18px;">Select an attack type to visualize how it targets an IoT network and learn the countermeasures from real security research.</p>
                    <div class="attack-grid" id="attack-grid"></div>
                    <canvas id="attack-canvas" height="260"></canvas>
                    <div class="attack-info" id="attack-info">
                        <h4 id="attack-info-title"></h4>
                        <p id="attack-info-desc"></p>
                        <p class="countermeasure" id="attack-info-counter"></p>
                    </div>
                </div>
            </div>
            <div id="panel-nn" class="lab-panel">
                <div class="lab-card">
                    <h2>🧠 Neural Network Visualizer</h2>
                    <p style="color:#999;font-size:0.92rem;margin-bottom:16px;">Build and animate a neural network. Watch signals propagate forward through layers — like in deep learning models for sensor data analysis.</p>
                    <div class="nn-controls">
                        <div><label>Hidden Layers: <span class="val" id="nn-layers-val">2</span></label><input type="range" id="nn-layers" min="1" max="5" value="2" step="1" oninput="document.getElementById('nn-layers-val').textContent=this.value;drawNN();"></div>
                        <div><label>Neurons/Layer: <span class="val" id="nn-neurons-val">4</span></label><input type="range" id="nn-neurons" min="2" max="8" value="4" step="1" oninput="document.getElementById('nn-neurons-val').textContent=this.value;drawNN();"></div>
                        <div><label>Architecture:</label>
                            <select id="nn-arch" onchange="drawNN()" style="background:#0a1628;color:#4fc3f7;border:1px solid #4fc3f7;border-radius:6px;padding:6px 10px;font-size:0.88rem;">
                                <option value="ffn">Feedforward (FFN)</option>
                                <option value="bilstm">BiLSTM</option>
                                <option value="cnn">CNN</option>
                            </select>
                        </div>
                        <button onclick="pulseNN()">Fire Signal</button>
                    </div>
                    <canvas id="nn-canvas" height="320"></canvas>
                    <div class="nn-info">
                        <div class="nn-info-item"><div class="label">Est. Parameters</div><div class="value" id="nn-params">—</div></div>
                        <div class="nn-info-item"><div class="label">Depth</div><div class="value" id="nn-depth">—</div></div>
                        <div class="nn-info-item"><div class="label">Architecture</div><div class="value" id="nn-arch-name">—</div></div>
                    </div>
                    <p style="color:#666;font-size:0.82rem;margin-top:14px;">The CNN-BiLSTM-Attention architecture used in real postural stability research combines convolutional feature extraction with bidirectional temporal learning.</p>
                </div>
            </div>
            <div id="panel-robot" class="lab-panel">
                <div class="lab-card">
                    <h2>🤖 Embodied AI — Robot Path Navigator</h2>
                    <p style="color:#999;font-size:0.92rem;margin-bottom:12px;">Click the grid to place obstacles, then watch the robot use A* pathfinding — the same algorithm used in autonomous robot navigation. Inject a cyber threat to see how attacks affect robot behaviour.</p>
                    <div class="robot-status" id="robot-status">🤖 Click on the grid to place obstacles. Then press Find Path.</div>
                    <div class="robot-controls">
                        <button onclick="robotFindPath()">Find Path (A*)</button>
                        <button onclick="robotReset()">Reset Grid</button>
                        <button onclick="robotRandomObstacles()">Random Obstacles</button>
                        <button class="danger" onclick="robotAddThreat()">Inject Cyber Threat</button>
                    </div>
                    <canvas id="robot-canvas" height="360" onclick="robotCanvasClick(event)"></canvas>
                    <div class="robot-legend">
                        <div class="robot-legend-item"><div class="robot-legend-dot" style="background:#4fc3f7"></div>Robot (R)</div>
                        <div class="robot-legend-item"><div class="robot-legend-dot" style="background:#a5d6a7"></div>Goal (G)</div>
                        <div class="robot-legend-item"><div class="robot-legend-dot" style="background:#37474f"></div>Obstacle</div>
                        <div class="robot-legend-item"><div class="robot-legend-dot" style="background:#f48fb1"></div>Planned Path</div>
                        <div class="robot-legend-item"><div class="robot-legend-dot" style="background:#f44336"></div>Cyber Threat (X)</div>
                    </div>
                </div>
            </div>
            <div id="panel-ttt" class="lab-panel">
                <div class="lab-card">
                    <h2>🎮 Tic Tac Toe</h2>
                    <div class="ttt-score-board">
                        <div class="ttt-score-item"><div class="s-label">Player X</div><div class="s-value" id="score-x">0</div></div>
                        <div class="ttt-score-item"><div class="s-label">Draws</div><div class="s-value" id="score-d">0</div></div>
                        <div class="ttt-score-item o-score"><div class="s-label">Player O / AI</div><div class="s-value" id="score-o">0</div></div>
                    </div>
                    <div class="ttt-controls">
                        <label><input type="radio" name="ttt-mode" value="human" checked> Human vs Human</label>
                        <label><input type="radio" name="ttt-mode" value="computer"> Human vs AI</label>
                    </div>
                    <div id="ttt-board"></div>
                    <p id="ttt-status">Select a mode and start playing!</p>
                    <button id="ttt-reset">Reset Game</button>
                </div>
            </div>
        </main>
        <footer>
            <div class="footer-logos">
                <img src="university_logo_orebro.png" alt="Orebro University Logo" class="footer-logo" />
                <img src="university_logo1.png" alt="University of Genoa Logo" class="footer-logo" />
                <img src="university_logo2.png" alt="CNIT Logo" class="footer-logo" />
                <img src="university_logo3.png" alt="COSMIC Lab Logo" class="footer-logo" />
                <img src="university_logo4.png" alt="DITEN Logo" class="footer-logo" />
                <img src="university_logo5.png" alt="KTH Royal Institute Logo" class="footer-logo" />
            </div>
            <p class="footer-copy">© 2026 Dr. Junaid Qadir. All rights reserved.</p>
        </footer>
    </div>
<script>
function showTab(name,btn){
    document.querySelectorAll('.lab-panel').forEach(function(p){p.classList.remove('active');});
    document.querySelectorAll('.lab-tab-btn').forEach(function(b){b.classList.remove('active');});
    document.getElementById('panel-'+name).classList.add('active');
    if(btn) btn.classList.add('active');
    if(name==='signal'&&!sigStarted) initSignal();
    if(name==='attack'&&!atkStarted) initAttack();
    if(name==='nn') drawNN();
    if(name==='robot'&&!robotStarted) initRobot();
}
var topics=['IoT and LoRaWAN Security','Cybersecurity for Embodied AI','Deep Learning and Neural Networks','Signal Processing and IMU Sensors','5G and 6G Networks','Explainable AI','Robot Security and Cyber-Physical Systems','General Cybersecurity'];
var currentTopic=topics[0],qStreak=0,qTotal=0,qCorrect=0,currentQ=null,qAnswered=false;
function initQuiz(){
    var bar=document.getElementById('quiz-topics');
    topics.forEach(function(t,i){
        var btn=document.createElement('button');
        btn.className='quiz-topic-btn'+(i===0?' active':'');
        btn.textContent=t;
        btn.onclick=function(){document.querySelectorAll('.quiz-topic-btn').forEach(function(b){b.classList.remove('active');});btn.classList.add('active');currentTopic=t;loadQuestion();};
        bar.appendChild(btn);
    });
    loadQuestion();
}
function loadQuestion(){
    document.getElementById('quiz-container').innerHTML='<div class="quiz-loading"><div class="spinner"></div><br>Generating question on <strong style="color:#4fc3f7">'+currentTopic+'</strong>...</div>';
    qAnswered=false;
    var prompt='You are a cybersecurity and AI quiz generator. Generate ONE multiple-choice question about: "'+currentTopic+'". Return ONLY a JSON object (no markdown, no extra text) in this exact format: {"q":"question text","opts":["A","B","C","D"],"ans":0,"exp":"brief explanation"} where ans is the index (0-3) of the correct option.';
    fetch("https://api.anthropic.com/v1/messages",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({model:"claude-sonnet-4-20250514",max_tokens:1000,messages:[{role:"user",content:prompt}]})})
    .then(function(r){return r.json();})
    .then(function(data){
        var raw=data.content[0].text.trim().replace(/```json|```/g,'').trim();
        currentQ=JSON.parse(raw);renderQuestion(currentQ);
    }).catch(function(){currentQ=getFallback();renderQuestion(currentQ);});
}
function getFallback(){
    var bank=[
        {q:"What does embodied AI mean?",opts:["AI in the cloud","AI in physical systems like robots","AI with emotions","AI trained on body data"],ans:1,exp:"Embodied AI refers to AI systems that physically interact with the world through sensors and actuators."},
        {q:"Which protocol is most used in IoT low-power wide-area networks?",opts:["HTTP","LoRaWAN","FTP","Bluetooth Classic"],ans:1,exp:"LoRaWAN is designed for low-power, long-range IoT communication."},
        {q:"What is a replay attack?",opts:["Crashing a server","Reusing a captured valid packet","Injecting malware","Physical destruction"],ans:1,exp:"A replay attack retransmits a valid captured packet to fool the receiver."},
        {q:"What does LSTM stand for?",opts:["Long Short-Term Memory","Linear Sequential Training Model","Large Scale Transfer Model","Layered Signal Transmission Module"],ans:0,exp:"LSTM is a recurrent neural network architecture for learning temporal dependencies."},
        {q:"What is the CIA triad?",opts:["Confidentiality Integrity Availability","Cyber Intelligence Attack","Control Identity Access","Confidentiality Interoperability Authentication"],ans:0,exp:"The CIA triad are the three core principles of information security."},
        {q:"What is NFV in 5G?",opts:["Network Function Virtualization","Node Frequency Validation","Network Firewall Version","Null Frame Verification"],ans:0,exp:"NFV decouples network functions from hardware, running them as software."},
        {q:"What is a sinkhole attack?",opts:["Flooding the network","A node attracting traffic with false routing info","Physically destroying sensors","Jamming frequencies"],ans:1,exp:"A sinkhole node falsely advertises the best route, attracting and dropping packets."},
    ];
    return bank[Math.floor(Math.random()*bank.length)];
}
function renderQuestion(q){
    var pct=qTotal>0?Math.round((qCorrect/qTotal)*100):0;
    document.getElementById('quiz-container').innerHTML='<div class="quiz-meta"><span>Topic: <strong style="color:#4fc3f7">'+currentTopic+'</strong></span><span>Score: '+qCorrect+'/'+qTotal+' ('+pct+'%)</span></div><div class="quiz-progress-bar"><div class="quiz-progress-fill" style="width:'+Math.min(pct,100)+'%"></div></div><div class="quiz-question">'+q.q+'</div><div class="quiz-options">'+q.opts.map(function(o,i){return '<button class="quiz-opt" onclick="answerQ('+i+')">'+o+'</button>';}).join('')+'</div><div class="quiz-feedback" id="quiz-feedback"></div><div class="quiz-nav"><button onclick="loadQuestion()" id="quiz-next" style="display:none">Next Question</button><div class="quiz-streak" id="quiz-streak">'+(qStreak>0?'Streak: '+qStreak:'')+'</div></div>';
}
function answerQ(i){
    if(qAnswered) return;
    qAnswered=true;qTotal++;
    var q=currentQ;
    document.querySelectorAll('.quiz-opt').forEach(function(o,idx){o.disabled=true;if(idx===q.ans)o.classList.add('correct');else if(idx===i&&i!==q.ans)o.classList.add('wrong');});
    var fb=document.getElementById('quiz-feedback');
    if(i===q.ans){qCorrect++;qStreak++;fb.innerHTML='<span style="color:#a5d6a7">Correct!</span> '+q.exp;}
    else{qStreak=0;fb.innerHTML='<span style="color:#ef9a9a">Incorrect.</span> '+q.exp;}
    document.getElementById('quiz-streak').textContent=qStreak>1?'🔥 Streak: '+qStreak:'';
    document.getElementById('quiz-next').style.display='inline-block';
}
initQuiz();
var sigStarted=false,sigT=0;
function initSignal(){
    sigStarted=true;
    var canvas=document.getElementById('sig-canvas');
    var ctx=canvas.getContext('2d');
    ['sig-freq','sig-amp','sig-noise','sig-comp2'].forEach(function(id){document.getElementById(id).addEventListener('input',updateSigLabels);});
    function frame(){
        var W=canvas.offsetWidth;canvas.width=W;canvas.height=220;
        var freq=parseFloat(document.getElementById('sig-freq').value);
        var amp=parseFloat(document.getElementById('sig-amp').value);
        var noise=parseFloat(document.getElementById('sig-noise').value);
        var comp2=parseFloat(document.getElementById('sig-comp2').value);
        ctx.clearRect(0,0,W,220);
        ctx.strokeStyle='rgba(79,195,247,0.08)';ctx.lineWidth=1;
        for(var y=0;y<=220;y+=44){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke();}
        for(var x=0;x<=W;x+=W/8){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,220);ctx.stroke();}
        var midY=110,scaleY=40/Math.max(amp+comp2,1);
        ctx.beginPath();ctx.strokeStyle='#4fc3f7';ctx.lineWidth=2;
        for(var i=0;i<W;i++){var xT=(i/W)*4*Math.PI+sigT;var cy=midY-(Math.sin(freq*xT)*amp+Math.sin(freq*2.3*xT)*comp2)*scaleY;i===0?ctx.moveTo(i,cy):ctx.lineTo(i,cy);}
        ctx.stroke();
        if(noise>0){ctx.beginPath();ctx.strokeStyle='#f48fb1';ctx.lineWidth=1.5;
        for(var i=0;i<W;i++){var xT=(i/W)*4*Math.PI+sigT;var n=(Math.random()-0.5)*2*noise;var cy=midY-(Math.sin(freq*xT)*amp+Math.sin(freq*2.3*xT)*comp2+n)*scaleY;i===0?ctx.moveTo(i,cy):ctx.lineTo(i,cy);}
        ctx.stroke();}
        document.getElementById('snr-val').textContent=noise>0?(20*Math.log10(amp/noise)).toFixed(1)+' dB':'inf dB';
        document.getElementById('peak-val').textContent=(amp+comp2).toFixed(2);
        document.getElementById('quality-val').textContent=noise<0.2?'Excellent':noise<0.8?'Moderate':'Poor';
        sigT+=0.02;requestAnimationFrame(frame);
    }
    frame();
}
function updateSigLabels(){
    document.getElementById('freq-val').textContent=document.getElementById('sig-freq').value+' Hz';
    document.getElementById('amp-val').textContent=document.getElementById('sig-amp').value;
    document.getElementById('noise-val').textContent=document.getElementById('sig-noise').value;
    var c=parseFloat(document.getElementById('sig-comp2').value);
    document.getElementById('comp2-val').textContent=c===0?'Off':c+'x';
}
var attacks=[
    {id:'replay',name:'Replay Attack',desc:'An attacker captures a valid LoRaWAN packet and retransmits it to trick the network server.',counter:'Countermeasure: Frame counters (FCnt) ensure each packet has a unique sequence — replayed packets are rejected.'},
    {id:'jamming',name:'Jamming Attack',desc:'The attacker floods the RF frequency with interference, blocking all legitimate device communication.',counter:'Countermeasure: Frequency hopping spread spectrum and redundant gateways reduce jamming impact.'},
    {id:'sinkhole',name:'Sinkhole Attack',desc:'A compromised node advertises a false optimal route, attracting all traffic and dropping packets.',counter:'Countermeasure: Trust-based routing and anomaly detection identify nodes with suspicious routing behaviour.'},
    {id:'mitm',name:'Man-in-the-Middle',desc:'An attacker intercepts communication between device and server, reading or modifying messages.',counter:'Countermeasure: End-to-end AES-128 encryption ensures confidentiality even if intercepted.'},
];
var atkStarted=false,atkAnimId=null;
function initAttack(){
    atkStarted=true;
    var grid=document.getElementById('attack-grid');
    attacks.forEach(function(a){
        var card=document.createElement('div');card.className='attack-card';
        card.innerHTML='<h4>'+a.name+'</h4><p>'+a.desc.substring(0,60)+'...</p>';
        card.onclick=function(){selectAttack(a,card);};grid.appendChild(card);
    });
    drawNetworkIdle();
}
function selectAttack(attack,card){
    document.querySelectorAll('.attack-card').forEach(function(c){c.classList.remove('selected');});card.classList.add('selected');
    document.getElementById('attack-info-title').textContent=attack.name;
    document.getElementById('attack-info-desc').textContent=attack.desc;
    document.getElementById('attack-info-counter').textContent=attack.counter;
    document.getElementById('attack-info').classList.add('visible');
    if(atkAnimId) cancelAnimationFrame(atkAnimId);
    var canvas=document.getElementById('attack-canvas');
    var W=canvas.offsetWidth;canvas.width=W;canvas.height=260;
    var ctx=canvas.getContext('2d');var t=0;
    function frame(){drawNetwork(ctx,W,260,attack.id,t++);atkAnimId=requestAnimationFrame(frame);}
    frame();
}
function drawNetworkIdle(){var canvas=document.getElementById('attack-canvas');var W=canvas.offsetWidth;canvas.width=W;canvas.height=260;drawNetwork(canvas.getContext('2d'),W,260,null,0);}
function drawNetwork(ctx,W,H,attackId,t){
    ctx.clearRect(0,0,W,H);
    var nodes={d1:{x:W*0.1,y:H*0.3,label:'Device 1'},d2:{x:W*0.1,y:H*0.75,label:'Device 2'},gw:{x:W*0.45,y:H*0.5,label:'Gateway'},srv:{x:W*0.85,y:H*0.5,label:'Server'}};
    if(attackId==='sinkhole') nodes.atk={x:W*0.45,y:H*0.12,label:'Sinkhole'};
    if(attackId==='mitm') nodes.atk={x:W*0.65,y:H*0.18,label:'Attacker'};
    var links=[['d1','gw'],['d2','gw'],['gw','srv']];
    if(attackId==='sinkhole'){links.push(['d1','atk']);links.push(['d2','atk']);}
    if(attackId==='mitm'){links.push(['atk','srv']);}
    links.forEach(function(pair){
        var na=nodes[pair[0]],nb=nodes[pair[1]];if(!na||!nb) return;
        var evil=(attackId==='sinkhole'&&pair[1]==='atk')||(attackId==='mitm'&&(pair[0]==='atk'||pair[1]==='atk'));
        ctx.beginPath();ctx.strokeStyle=evil?'rgba(244,67,54,0.6)':'rgba(79,195,247,0.3)';ctx.lineWidth=evil?2:1.5;ctx.setLineDash(evil?[6,4]:[]);
        ctx.moveTo(na.x,na.y);ctx.lineTo(nb.x,nb.y);ctx.stroke();ctx.setLineDash([]);
    });
    if(attackId&&t>0){
        var prog=(t%100)/100;
        var p1=nodes.d1,p2=nodes.gw;
        ctx.beginPath();ctx.arc(p1.x+(p2.x-p1.x)*prog,p1.y+(p2.y-p1.y)*prog,6,0,Math.PI*2);
        ctx.fillStyle=(attackId==='replay'||attackId==='jamming')?'#f44336':'#4fc3f7';ctx.fill();
        if(attackId==='replay'&&prog>0.5){var rp=(prog-0.5)/0.5;ctx.beginPath();ctx.arc(p1.x+(p2.x-p1.x)*rp,p1.y+(p2.y-p1.y)*rp,6,0,Math.PI*2);ctx.fillStyle='#ff8a65';ctx.fill();}
        if(attackId==='jamming'){for(var i=0;i<6;i++){var a=(t*0.05+i*(Math.PI*2/6))%(Math.PI*2);var r=26+Math.sin(t*0.1)*6;ctx.beginPath();ctx.arc(nodes.gw.x+Math.cos(a)*r,nodes.gw.y+Math.sin(a)*r,4,0,Math.PI*2);ctx.fillStyle='rgba(244,67,54,0.5)';ctx.fill();}}
    }
    Object.values(nodes).forEach(function(n){
        var evil=n.label==='Sinkhole'||n.label==='Attacker';
        ctx.beginPath();ctx.arc(n.x,n.y,18,0,Math.PI*2);
        ctx.fillStyle=evil?'rgba(244,67,54,0.2)':'rgba(79,195,247,0.12)';
        ctx.strokeStyle=evil?'#f44336':'#4fc3f7';ctx.lineWidth=2;ctx.fill();ctx.stroke();
        ctx.fillStyle=evil?'#f44336':'#4fc3f7';ctx.font='bold 9px sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';
        ctx.fillText(n.label.substring(0,7),n.x,n.y);
        ctx.fillStyle='#888';ctx.font='9px sans-serif';ctx.fillText(n.label,n.x,n.y+28);
    });
}
var nnPulses=[];
function drawNN(){
    var canvas=document.getElementById('nn-canvas');
    var W=canvas.offsetWidth;canvas.width=W;canvas.height=320;
    var ctx=canvas.getContext('2d');
    var layers=parseInt(document.getElementById('nn-layers').value);
    var neurons=parseInt(document.getElementById('nn-neurons').value);
    var arch=document.getElementById('nn-arch').value;
    var archNames={ffn:'Feedforward (FFN)',bilstm:'BiLSTM',cnn:'CNN'};
    var inputN=4,outputN=2;
    var allLayers=[inputN];for(var i=0;i<layers;i++) allLayers.push(neurons);allLayers.push(outputN);
    var totalParams=allLayers.reduce(function(s,n,i){return i>0?s+allLayers[i-1]*n+n:s;},0);
    document.getElementById('nn-params').textContent=totalParams.toLocaleString();
    document.getElementById('nn-depth').textContent=(layers+2)+' layers';
    document.getElementById('nn-arch-name').textContent=archNames[arch];
    ctx.clearRect(0,0,W,320);
    var xStep=W/(allLayers.length+1);
    var positions=[];
    allLayers.forEach(function(n,li){
        var x=xStep*(li+1);var yStep=260/(n+1);var lp=[];
        for(var ni=0;ni<n;ni++){lp.push({x:x,y:30+yStep*(ni+1)});}
        positions.push(lp);
    });
    for(var li=0;li<positions.length-1;li++){
        positions[li].forEach(function(src){positions[li+1].forEach(function(dst){ctx.beginPath();ctx.strokeStyle='rgba(79,195,247,0.07)';ctx.lineWidth=0.8;ctx.moveTo(src.x,src.y);ctx.lineTo(dst.x,dst.y);ctx.stroke();});});
    }
    nnPulses.forEach(function(p){
        if(p.li>=positions.length-1||p.ni>=positions[p.li].length||p.nextNi>=positions[p.li+1].length) return;
        var src=positions[p.li][p.ni],dst=positions[p.li+1][p.nextNi];
        var px=src.x+(dst.x-src.x)*p.progress,py=src.y+(dst.y-src.y)*p.progress;
        ctx.beginPath();ctx.arc(px,py,4,0,Math.PI*2);ctx.fillStyle='rgba(79,195,247,'+(0.9-p.progress*0.5)+')';ctx.fill();
    });
    positions.forEach(function(layer,li){
        var isInput=li===0,isOutput=li===positions.length-1;
        var color=isInput?'#81c784':isOutput?'#f48fb1':'#4fc3f7';
        var label=isInput?'Input':isOutput?'Output':arch==='bilstm'?'BiLSTM':arch==='cnn'?'Conv':'Hidden';
        layer.forEach(function(n){ctx.beginPath();ctx.arc(n.x,n.y,11,0,Math.PI*2);ctx.fillStyle='rgba(79,195,247,0.1)';ctx.strokeStyle=color;ctx.lineWidth=2;ctx.fill();ctx.stroke();});
        ctx.fillStyle=color;ctx.font='10px sans-serif';ctx.textAlign='center';ctx.fillText(label,xStep*(li+1),305);
    });
}
function pulseNN(){
    var layers=parseInt(document.getElementById('nn-layers').value);
    var neurons=parseInt(document.getElementById('nn-neurons').value);
    var allLayers=[4];for(var i=0;i<layers;i++) allLayers.push(neurons);allLayers.push(2);
    nnPulses=[];var delay=0;
    for(var li=0;li<allLayers.length-1;li++){
        for(var ni=0;ni<allLayers[li];ni++){
            for(var nni=0;nni<allLayers[li+1];nni++){
                if(Math.random()<0.35) nnPulses.push({li:li,ni:ni,nextNi:nni,progress:0,delay:delay});
            }
        }
        delay+=18;
    }
    var frame=0;
    function animate(){
        nnPulses.forEach(function(p){if(frame>=p.delay) p.progress=Math.min(1,(frame-p.delay)/30);});
        drawNN();
        for(var i=nnPulses.length-1;i>=0;i--){if(nnPulses[i].progress>=1) nnPulses.splice(i,1);}
        if(nnPulses.length>0) requestAnimationFrame(animate);
        frame++;
    }
    animate();
}
var COLS=18,ROWS=12,robotGrid=[],robotPath=[],robotStarted=false,robotThreat=null;
var START={r:6,c:0},GOAL={r:6,c:17};
function initRobot(){robotStarted=true;robotGrid=Array.from({length:ROWS},function(){return Array(COLS).fill(0);});drawRobot();}
function robotReset(){robotGrid=Array.from({length:ROWS},function(){return Array(COLS).fill(0);});robotPath=[];robotThreat=null;document.getElementById('robot-status').textContent='Grid reset. Click to place obstacles, then press Find Path.';drawRobot();}
function robotRandomObstacles(){
    robotGrid=Array.from({length:ROWS},function(){return Array(COLS).fill(0);});robotPath=[];robotThreat=null;
    for(var i=0;i<35;i++){var r=Math.floor(Math.random()*ROWS),c=Math.floor(Math.random()*COLS);if((r===START.r&&c===START.c)||(r===GOAL.r&&c===GOAL.c)) continue;robotGrid[r][c]=1;}
    document.getElementById('robot-status').textContent='Random obstacles placed. Press Find Path!';drawRobot();
}
function robotAddThreat(){
    var r=Math.floor(Math.random()*ROWS),c=1+Math.floor(Math.random()*(COLS-2));
    robotThreat={r:r,c:c};
    document.getElementById('robot-status').textContent='Cyber threat injected at node ('+r+','+c+'). The robot will try to avoid it.';
    if(robotPath.length>0) robotFindPath();else drawRobot();
}
function robotCanvasClick(e){
    var canvas=document.getElementById('robot-canvas');
    var rect=canvas.getBoundingClientRect();
    var fc=Math.floor((e.clientX-rect.left)/(canvas.offsetWidth/COLS));
    var fr=Math.floor((e.clientY-rect.top)/(canvas.offsetHeight/ROWS));
    if(fr<0||fr>=ROWS||fc<0||fc>=COLS) return;
    if((fr===START.r&&fc===START.c)||(fr===GOAL.r&&fc===GOAL.c)) return;
    robotGrid[fr][fc]=robotGrid[fr][fc]===1?0:1;robotPath=[];drawRobot();
}
function robotFindPath(){
    function key(r,c){return r+','+c;}
    function h(r,c){return Math.abs(r-GOAL.r)+Math.abs(c-GOAL.c);}
    var open=new Map();open.set(key(START.r,START.c),{r:START.r,c:START.c,g:0,f:h(START.r,START.c),parent:null});
    var closed=new Set();var found=null;
    while(open.size>0){
        var cur=null;open.forEach(function(n){if(!cur||n.f<cur.f) cur=n;});
        if(cur.r===GOAL.r&&cur.c===GOAL.c){found=cur;break;}
        open.delete(key(cur.r,cur.c));closed.add(key(cur.r,cur.c));
        [[0,1],[0,-1],[1,0],[-1,0]].forEach(function(d){
            var nr=cur.r+d[0],nc=cur.c+d[1];
            if(nr<0||nr>=ROWS||nc<0||nc>=COLS||robotGrid[nr][nc]===1||closed.has(key(nr,nc))) return;
            var threat=(robotThreat&&robotThreat.r===nr&&robotThreat.c===nc)?500:0;
            var ng=cur.g+1+threat,nf=ng+h(nr,nc);
            var ex=open.get(key(nr,nc));
            if(!ex||ng<ex.g) open.set(key(nr,nc),{r:nr,c:nc,g:ng,f:nf,parent:cur});
        });
    }
    if(found){
        robotPath=[];var n=found;while(n){robotPath.unshift({r:n.r,c:n.c});n=n.parent;}
        var avd=robotThreat&&!robotPath.some(function(p){return p.r===robotThreat.r&&p.c===robotThreat.c;});
        document.getElementById('robot-status').textContent='Path found! Length: '+robotPath.length+' steps.'+(avd?' Threat node avoided!':'');
    } else {
        robotPath=[];document.getElementById('robot-status').textContent='No path found — all routes blocked!';
    }
    drawRobot();
}
function drawRobot(){
    var canvas=document.getElementById('robot-canvas');
    var W=canvas.offsetWidth;canvas.width=W;canvas.height=360;
    var ctx=canvas.getContext('2d');
    var cw=W/COLS,ch=360/ROWS;
    ctx.clearRect(0,0,W,360);
    var pathSet=new Set(robotPath.map(function(p){return p.r+','+p.c;}));
    for(var r=0;r<ROWS;r++){for(var c=0;c<COLS;c++){
        var x=c*cw,y=r*ch;
        var isStart=r===START.r&&c===START.c;
        var isGoal=r===GOAL.r&&c===GOAL.c;
        var isWall=robotGrid[r][c]===1;
        var isThreat=robotThreat&&robotThreat.r===r&&robotThreat.c===c;
        var isPath=pathSet.has(r+','+c)&&!isStart&&!isGoal;
        ctx.fillStyle=isWall?'#263238':isThreat?'rgba(244,67,54,0.35)':isStart?'rgba(79,195,247,0.25)':isGoal?'rgba(165,214,167,0.25)':isPath?'rgba(244,143,177,0.2)':'rgba(255,255,255,0.02)';
        ctx.fillRect(x+1,y+1,cw-2,ch-2);
        ctx.strokeStyle='rgba(79,195,247,0.07)';ctx.lineWidth=0.5;ctx.strokeRect(x,y,cw,ch);
        ctx.font='bold '+(Math.min(cw,ch)*0.55)+'px sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';
        if(isStart){ctx.fillStyle='#4fc3f7';ctx.fillText('R',x+cw/2,y+ch/2);}
        if(isGoal){ctx.fillStyle='#a5d6a7';ctx.fillText('G',x+cw/2,y+ch/2);}
        if(isThreat&&!isWall){ctx.fillStyle='#f44336';ctx.fillText('X',x+cw/2,y+ch/2);}
    }}
    if(robotPath.length>1){
        ctx.beginPath();ctx.strokeStyle='rgba(244,143,177,0.7)';ctx.lineWidth=2;
        robotPath.forEach(function(p,i){var x=p.c*cw+cw/2,y=p.r*ch+ch/2;i===0?ctx.moveTo(x,y):ctx.lineTo(x,y);});
        ctx.stroke();
    }
}
var tttBoard=Array(9).fill(null),tttTurn='X',tttRunning=false;
var scores={X:0,O:0,D:0};
var wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
function tttInit(){tttBoard=Array(9).fill(null);tttTurn='X';tttRunning=true;renderTTT();document.getElementById('ttt-status').textContent="Player X's turn";}
function renderTTT(){
    var board=document.getElementById('ttt-board');board.innerHTML='';
    tttBoard.forEach(function(val,i){
        var cell=document.createElement('div');
        cell.className='ttt-cell'+(val?' taken':'')+(val==='O'?' o-cell':'');
        cell.textContent=val||'';cell.onclick=function(){tttClick(i);};board.appendChild(cell);
    });
}
function tttClick(i){
    if(!tttRunning||tttBoard[i]) return;
    tttBoard[i]=tttTurn;renderTTT();
    var w=checkWin();
    if(w){highlightWin(w);endGame(tttTurn+' wins!');scores[tttTurn]++;updateScores();return;}
    if(tttBoard.every(function(c){return c;})){endGame("It's a draw!");scores.D++;updateScores();return;}
    tttTurn=tttTurn==='X'?'O':'X';
    document.getElementById('ttt-status').textContent='Player '+tttTurn+"'s turn";
    if(document.querySelector('input[name="ttt-mode"]:checked').value==='computer'&&tttTurn==='O') setTimeout(aiMove,400);
}
function aiMove(){
    var best=minimax(tttBoard,'O');
    tttBoard[best.idx]='O';renderTTT();
    var w=checkWin();
    if(w){highlightWin(w);endGame('AI wins!');scores.O++;updateScores();return;}
    if(tttBoard.every(function(c){return c;})){endGame("It's a draw!");scores.D++;updateScores();return;}
    tttTurn='X';document.getElementById('ttt-status').textContent="Player X's turn";
}
function minimax(board,player){
    var w=checkWinFor(board);
    if(w==='O') return{score:10};if(w==='X') return{score:-10};
    var empty=board.map(function(v,i){return v===null?i:-1;}).filter(function(i){return i>=0;});
    if(!empty.length) return{score:0};
    var moves=empty.map(function(i){var b=board.slice();b[i]=player;var s=minimax(b,player==='O'?'X':'O').score;return{idx:i,score:s};});
    return player==='O'?moves.reduce(function(a,b){return b.score>a.score?b:a;}):moves.reduce(function(a,b){return b.score<a.score?b:a;});
}
function checkWin(){return wins.find(function(c){return tttBoard[c[0]]&&tttBoard[c[0]]===tttBoard[c[1]]&&tttBoard[c[0]]===tttBoard[c[2]];})||null;}
function checkWinFor(b){var w=wins.find(function(c){return b[c[0]]&&b[c[0]]===b[c[1]]&&b[c[0]]===b[c[2]];});return w?b[w[0]]:null;}
function highlightWin(combo){document.querySelectorAll('.ttt-cell').forEach(function(c,i){if(combo.indexOf(i)>=0)c.classList.add('win-cell');});}
function endGame(msg){tttRunning=false;document.getElementById('ttt-status').textContent=msg;}
function updateScores(){document.getElementById('score-x').textContent=scores.X;document.getElementById('score-o').textContent=scores.O;document.getElementById('score-d').textContent=scores.D;}
document.getElementById('ttt-reset').onclick=tttInit;
tttInit();
</script>
</body>
</html>'''

with open('interactive-lab.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("interactive-lab.html written successfully!")
