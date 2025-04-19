function startCountdown(targetISO) {
    const endTime = new Date(targetISO);
    const countdownEl = document.getElementById('countdown');

    function updateCountdown() {
      const now = new Date();
      let delta = endTime - now;

      if (delta <= 0) {
        countdownEl.textContent = "⏳ Time's up!";
        clearInterval(timer);
        return;
      }
      let ms = delta % 1000;
      ms = String(ms).padStart(3, '0');
      delta = Math.floor(delta / 1000);  // convert to seconds
      let sec = String(delta % 60).padStart(2, '0');
      delta = Math.floor(delta / 60);
      let min = String(delta % 60).padStart(2, '0');
      delta = Math.floor(delta / 60);
      let hr = String(delta % 24).padStart(2, '0');
      delta = Math.floor(delta / 24);
      let days = String(delta % 365);
      let years = String(Math.floor(delta / 365));

      countdownEl.textContent = `${years}y:${days}d:${hr}h:${min}m:${sec}s:${ms}ms`;
    }

    const timer = setInterval(updateCountdown, 50);
  }

  // Start using date we injected in the countdown.html
  startCountdown(window.targetDate);