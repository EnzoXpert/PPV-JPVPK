## analyze then think and reasecarh then redesign whole thing but keep the colour and add animation sound with colourfull   animated  gradiont  background 

I have analyzed the files and will now provide a redesigned `lucky-draw.html` that incorporates the requested features: a colorful animated gradient background, animation sounds, and a fresh design that respects the original color scheme.

Here is the updated and redesigned `lucky-draw.html` file:

```html
<!DOCTYPE html>
<html lang="ms">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mini Konvensyen Lucky Draw 2025</title>
    <meta name="description" content="Mini Konvensyen Lucky Draw 2025 - Sistem Cabutan Bertuah">
    <link rel="icon" href="https://www.jpvpk.gov.my/images/favicon.ico">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&family=Roboto:wght@400;700&display=swap" rel="stylesheet">

    <style>
        :root {
            --primary: #ff3366;
            --secondary: #cc0033;
            --gold-solid: #ffd700;
            --dark: #000033;
            --white: #ffffff;
            --radius-sm: 8px;
            --radius-md: 12px;
            --radius-lg: 16px;
            --transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Roboto', sans-serif;
        }

        body {
            background-color: var(--dark);
            color: var(--white);
            min-height: 100vh;
            overflow-x: hidden;
            text-align: center;
        }

        .animated-gradient-background {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            background: linear-gradient(45deg, var(--primary), var(--secondary), var(--gold-solid), var(--dark));
            background-size: 400% 400%;
            animation: gradientAnimation 15s ease infinite;
        }

        @keyframes gradientAnimation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .container {
            max-width: 1100px;
            margin: 0 auto;
            padding: 2rem 1rem;
        }

        header {
            margin-bottom: 2rem;
        }

        .logo {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            box-shadow: 0 0 20px rgba(255, 215, 0, .25);
            margin-bottom: 1rem;
        }

        h1 {
            font-family: 'Poppins', sans-serif;
            font-size: clamp(2rem, 5vw, 3rem);
            font-weight: 800;
            color: var(--gold-solid);
            text-shadow: 0 0 15px rgba(255, 215, 0, 0.5);
        }

        .page {
            display: none;
            flex-direction: column;
            align-items: center;
            gap: 1.5rem;
            animation: fadeIn 0.5s ease-out;
        }

        .page.active {
            display: flex;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .card {
            background: rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(10px);
            border-radius: var(--radius-lg);
            padding: 2rem;
            width: 100%;
            max-width: 500px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }

        button, .btn {
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            border: none;
            color: var(--white);
            padding: 1rem 2rem;
            border-radius: var(--radius-md);
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition);
            box-shadow: 0 4px 15px rgba(0,0,0,.2);
            text-transform: uppercase;
            letter-spacing: 1px;
            font-family: 'Poppins', sans-serif;
        }

        button:hover, .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,.3);
        }
        
        button:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }

        input, textarea {
            width: 100%;
            padding: 1rem;
            border-radius: var(--radius-sm);
            border: 1px solid rgba(255, 255, 255, 0.1);
            background: rgba(255, 255, 255, 0.05);
            color: var(--white);
            margin-bottom: 1rem;
            font-size: 1rem;
        }

        .wheel-container {
            position: relative;
            width: min(500px, 90vw);
            height: min(500px, 90vw);
            margin: 2rem auto;
        }
        
        #wheelCanvas {
            width: 100%;
            height: 100%;
        }

        .winner-announcement {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(0,0,0,.8);
            backdrop-filter: blur(10px);
            padding: 3rem;
            border-radius: var(--radius-lg);
            z-index: 1000;
            animation: popIn 0.3s ease-out;
        }

        .winner-name {
            font-size: 2.5rem;
            font-weight: bold;
            color: var(--gold-solid);
            margin-top: 1rem;
            margin-bottom: 2rem;
        }

        @keyframes popIn {
            from { opacity: 0; transform: translate(-50%, -50%) scale(0.8); }
            to { opacity: 1; transform: translate(-50%, -50%) scale(1); }
        }

        .confetti-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 999;
            pointer-events: none;
        }

    </style>
</head>
<body>
    <div class="animated-gradient-background"></div>
    <canvas class="confetti-canvas" id="confetti-canvas"></canvas>

    <div class="container">
        <header>
            <img class="logo" src="https://www.jpvpk.gov.my/images/2023/logo-jpvpk.png" alt="logo">
            <h1>Mini Konvensyen Lucky Draw</h1>
        </header>

        <div id="menuPage" class="page active">
            <div class="card">
                <h2>Selamat Datang</h2>
                <p>Sistem Cabutan Bertuah Mini Konvensyen PPV JPV PERAK</p>
                <div style="margin-top: 2rem; display: flex; flex-direction: column; gap: 1rem;">
                    <button onclick="showPage('wheelPage')">Mula Cabutan</button>
                    <button onclick="showPage('manualPage')">Tambah Peserta</button>
                    <button onclick="showWinnersList()">Lihat Pemenang</button>
                </div>
            </div>
        </div>

        <div id="manualPage" class="page">
            <div class="card">
                <h2>Tambah Peserta</h2>
                <input id="nameInput" placeholder="Masukkan nama">
                <textarea id="bulkInput" placeholder="Atau masukkan senarai nama, satu per baris"></textarea>
                <button onclick="addParticipants()">Tambah</button>
                <button onclick="showMenu()" style="background: grey; margin-top: 1rem;">Kembali</button>
            </div>
        </div>

        <div id="wheelPage" class="page">
            <div class="wheel-container">
                <canvas id="wheelCanvas" width="500" height="500"></canvas>
            </div>
            <p>Sedia untuk memutar roda?</p>
            <button id="spinButton" onclick="spinWheel()">Putar!</button>
            <button onclick="showMenu()" style="background: grey; margin-top: 1rem;">Kembali</button>
        </div>

        <div id="winnersPage" class="page">
            <div class="card">
                <h2>Senarai Pemenang</h2>
                <ul id="winnersList"></ul>
                <button onclick="showMenu()" style="background: grey; margin-top: 1rem;">Kembali</button>
            </div>
        </div>
    </div>

    <div id="winnerTemplate" style="display:none;">
        <div class="winner-announcement">
            <h2>Tahniah!</h2>
            <div class="winner-name"></div>
            <button onclick="closeWinnerAnnouncement()">Tutup</button>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/howler/2.2.3/howler.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>

    <script>
        let participants = [];
        let winners = [];
        let wheel;
        const GOOGLE_SHEET_CSV = 'https://docs.google.com/spreadsheets/d/1xljccIdU9wDqo8DC4mEkx6bo1b3Ak8s0ZXSYGoVa0Dk/export?format=csv';

        const sounds = {
            spin: new Howl({src:['https://assets.mixkit.co/active_storage/sfx/2003/2003-preview.mp3'], loop:true, volume:0.5}),
            win: new Howl({src:['https://assets.mixkit.co/active_storage/sfx/1435/1435-preview.mp3'], volume:0.8}),
            click: new Howl({src:['https://assets.mixkit.co/active_storage/sfx/2571/2571-preview.mp3'], volume:0.5}),
            add: new Howl({src:['https://assets.mixkit.co/sfx/preview/mixkit-software-interface-start-2574.mp3'], volume:0.5})
        };

        function showPage(id) {
            sounds.click.play();
            document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
            document.getElementById(id).classList.add('active');
        }

        function showMenu() {
            showPage('menuPage');
        }

        class SpinningWheel {
            constructor(canvas, participants) {
                this.canvas = canvas;
                this.ctx = canvas.getContext('2d');
                this.participants = participants;
                this.angle = 0;
                this.spinSpeed = 0;
                this.isSpinning = false;
            }

            draw() {
                this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
                const arc = (2 * Math.PI) / this.participants.length;
                this.participants.forEach((p, i) => {
                    this.ctx.beginPath();
                    this.ctx.fillStyle = i % 2 === 0 ? 'var(--primary)' : 'var(--secondary)';
                    this.ctx.moveTo(250, 250);
                    this.ctx.arc(250, 250, 250, i * arc, (i + 1) * arc);
                    this.ctx.fill();

                    this.ctx.save();
                    this.ctx.fillStyle = 'white';
                    this.ctx.translate(250, 250);
                    this.ctx.rotate(i * arc + arc / 2);
                    this.ctx.textAlign = 'right';
                    this.ctx.fillText(p.name, 230, 10);
                    this.ctx.restore();
                });
            }
        }
        
        async function loadParticipantsFromSheet() {
            try {
                const res = await fetch(GOOGLE_SHEET_CSV);
                if (!res.ok) throw new Error('Network response was not ok');
                const txt = await res.text();
                const rows = txt.split('\n').slice(1);
                rows.forEach(row => {
                    const [name, district] = row.split(',');
                    if(name) {
                        participants.push({ name: name.trim(), district: district ? district.trim() : '' });
                    }
                });
            } catch (err) {
                console.error('Failed to load participants:', err);
            }
        }

        function addParticipants() {
            sounds.add.play();
            const nameInput = document.getElementById('nameInput');
            const bulkInput = document.getElementById('bulkInput');
            if (nameInput.value) {
                participants.push({ name: nameInput.value, district: '' });
                nameInput.value = '';
            }
            if (bulkInput.value) {
                bulkInput.value.split('\n').forEach(name => {
                    if(name.trim()) participants.push({ name: name.trim(), district: '' });
                });
                bulkInput.value = '';
            }
            buildWheel();
        }

        function buildWheel() {
            const canvas = document.getElementById('wheelCanvas');
            if (!canvas) return;
            wheel = new SpinningWheel(canvas, participants.length > 0 ? participants : [{ name: "Add Participants", district: '' }]);
            wheel.draw();
        }

        function spinWheel() {
            if (participants.length === 0) {
                alert("Please add participants before spinning.");
                return;
            }
            if (wheel.isSpinning) return;
            
            sounds.spin.play();
            document.getElementById('spinButton').disabled = true;
            wheel.isSpinning = true;

            const spinTo = Math.random() * 360;
            const duration = 5; // seconds

            gsap.to(wheel.canvas, {
                rotation: `+=${360 * 5 + spinTo}`,
                duration: duration,
                ease: "power2.out",
                onComplete: () => announceWinner(spinTo)
            });
        }

        function announceWinner(finalAngle) {
            sounds.spin.stop();
            sounds.win.play();
            
            const degreesPerParticipant = 360 / participants.length;
            const winnerIndex = Math.floor(((360 - (finalAngle % 360)) / degreesPerParticipant));
            const winner = participants.splice(winnerIndex, 1)[0];
            winners.push(winner);

            const tpl = document.getElementById('winnerTemplate').innerHTML;
            const winnerEl = document.createElement('div');
            winnerEl.innerHTML = tpl;
            winnerEl.id = 'currentWinner';
            winnerEl.querySelector('.winner-name').textContent = winner.name;
            document.body.appendChild(winnerEl);

            confetti({
                particleCount: 150,
                spread: 90,
                origin: { y: 0.6 }
            });
            buildWheel();
            document.getElementById('spinButton').disabled = false;
        }

        function closeWinnerAnnouncement() {
            sounds.click.play();
            document.getElementById('currentWinner').remove();
        }

        function showWinnersList() {
            showPage('winnersPage');
            const list = document.getElementById('winnersList');
            list.innerHTML = '';
            winners.forEach(w => {
                const li = document.createElement('li');
                li.textContent = w.name;
                list.appendChild(li);
            });
        }

        window.onload = async () => {
            await loadParticipantsFromSheet();
            buildWheel();
        };
    </script>
</body>
</html>
```