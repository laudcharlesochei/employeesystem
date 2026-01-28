console.log('JavaScript loaded successfully!');

document.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('messageBtn');
  const msg = document.getElementById('message');

  if (btn && msg) {
    btn.addEventListener('click', () => {
      msg.textContent = 'Button clicked!';
    });

    btn.addEventListener('mouseover', () => {
      btn.style.opacity = '0.9';
    });

    btn.addEventListener('mouseout', () => {
      btn.style.opacity = '1';
    });
  }
});
