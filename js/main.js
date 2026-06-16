/* ============================================================
   Kent Tools - Main JavaScript
   ============================================================ */

/* --- Kill Google Translate banner only (NOT translation content) --- */
(function killGoogleBanner() {
  function removeBanner() {
    // ONLY target the banner frame — never touch .skiptranslate or translation iframes
    var frames = document.querySelectorAll('.goog-te-banner-frame, iframe.goog-te-banner-frame');
    frames.forEach(function(f) {
      if (f.parentNode) f.parentNode.removeChild(f);
    });
    // Fix body offset caused by banner
    if (document.body && document.body.style.top && document.body.style.top !== '0px') {
      document.body.style.top = '0px';
    }
  }
  removeBanner();
  var count = 0;
  var interval = setInterval(function() {
    removeBanner();
    if (++count > 60) clearInterval(interval);
  }, 200);
  document.addEventListener('DOMContentLoaded', function() {
    var obs = new MutationObserver(removeBanner);
    obs.observe(document.documentElement, { childList: true, subtree: true });
    setTimeout(function() { obs.disconnect(); }, 15000);
  });
})();

document.addEventListener('DOMContentLoaded', () => {

  // --- Mobile Nav Toggle ---
  const toggle = document.querySelector('.mobile-toggle');
  const nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      nav.classList.toggle('active');
      toggle.classList.toggle('open');
    });
  }

  // --- Scroll Fade-In ---
  const fadeEls = document.querySelectorAll('.fade-in');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, { threshold: 0.15 });
  fadeEls.forEach(el => observer.observe(el));

  // --- Active Nav Highlight ---
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html') || (currentPath === '/' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  // --- Contact Form (Formspree — replace with your own endpoint) ---
  const contactForm = document.getElementById('inquiry-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const btn = contactForm.querySelector('button[type="submit"]');
      const originalText = btn.textContent;
      btn.textContent = 'Sending...';
      btn.disabled = true;

      // Web3Forms endpoint — no change needed, form submits to https://api.web3forms.com/submit
      const formData = new FormData(contactForm);

      fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        body: formData
      })
      .then(response => {
        if (response.ok) {
          alert('Thank you! Your inquiry has been sent. We will reply within 12 hours.');
          contactForm.reset();
        } else {
          alert('Please contact us directly:\nContact: Kent\nEmail: kent@gezhi.group\nWhatsApp: +995 593 583 830');
        }
      })
      .catch(() => {
        alert('Please contact us directly:\nContact: Kent\nEmail: kent@gezhi.group\nWhatsApp: +995 593 583 830');
      })
      .finally(() => {
        btn.textContent = originalText;
        btn.disabled = false;
      });
    });
  }

  // --- Inject Floating Contact Buttons ---
  const floatingHTML = `
    <div class="floating-contact">
      <a href="https://wa.me/995593583830" target="_blank" rel="noopener" class="floating-btn floating-whatsapp" aria-label="Chat on WhatsApp">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
        <span class="floating-tooltip">WhatsApp</span>
      </a>
      <a href="mailto:kent@gezhi.group" class="floating-btn floating-email" aria-label="Send Email">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
        <span class="floating-tooltip">Email Kent</span>
      </a>
    </div>
  `;
  document.body.insertAdjacentHTML('beforeend', floatingHTML);

  // --- Smooth scroll for anchor links ---
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href === '#') return;
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
        if (nav && nav.classList.contains('active')) {
          nav.classList.remove('active');
          toggle.classList.remove('open');
        }
      }
    });
  });

  // --- Product Image Carousel ---
  initCarousels();

});

/* ============================================================
   Carousel Engine
   ============================================================ */
function initCarousels() {
  document.querySelectorAll('.carousel').forEach(carousel => {
    const track = carousel.querySelector('.carousel-track');
    const slides = carousel.querySelectorAll('.carousel-slide');
    const prevBtn = carousel.querySelector('.carousel-prev');
    const nextBtn = carousel.querySelector('.carousel-next');
    const dotsContainer = carousel.querySelector('.carousel-dots');

    if (!track || slides.length === 0) return;

    let currentIndex = 0;
    let isTransitioning = false;

    // Build dots
    if (slides.length > 1) {
      dotsContainer.innerHTML = '';
      slides.forEach((_, i) => {
        const dot = document.createElement('button');
        dot.className = 'carousel-dot' + (i === 0 ? ' active' : '');
        dot.setAttribute('aria-label', 'Go to image ' + (i + 1));
        dot.addEventListener('click', () => goTo(i));
        dotsContainer.appendChild(dot);
      });
    }

    function updateDots() {
      const dots = dotsContainer.querySelectorAll('.carousel-dot');
      dots.forEach((d, i) => d.classList.toggle('active', i === currentIndex));
    }

    function goTo(index) {
      if (isTransitioning || index === currentIndex) return;
      if (index < 0) index = slides.length - 1;
      if (index >= slides.length) index = 0;
      isTransitioning = true;
      currentIndex = index;
      track.style.transform = 'translateX(-' + (currentIndex * 100) + '%)';
      updateDots();
      setTimeout(() => { isTransitioning = false; }, 420);
    }

    function goNext() { goTo(currentIndex + 1); }
    function goPrev() { goTo(currentIndex - 1); }

    if (slides.length > 1) {
      prevBtn.addEventListener('click', goPrev);
      nextBtn.addEventListener('click', goNext);

      // Touch / swipe
      let touchStartX = 0;
      let touchStartY = 0;
      let touchMoved = false;

      carousel.addEventListener('touchstart', (e) => {
        if (e.touches.length === 1) {
          touchStartX = e.touches[0].clientX;
          touchStartY = e.touches[0].clientY;
          touchMoved = false;
        }
      }, { passive: true });

      carousel.addEventListener('touchmove', (e) => {
        if (e.touches.length === 1) {
          const dx = e.touches[0].clientX - touchStartX;
          const dy = e.touches[0].clientY - touchStartY;
          if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 5) {
            touchMoved = true;
            carousel.classList.add('swiping');
          }
        }
      }, { passive: true });

      carousel.addEventListener('touchend', (e) => {
        carousel.classList.remove('swiping');
        if (!touchMoved) return;
        const dx = e.changedTouches[0].clientX - touchStartX;
        if (Math.abs(dx) > 40) {
          dx > 0 ? goPrev() : goNext();
        }
      });

      // Mouse drag (desktop)
      let mouseDown = false;
      let mouseStartX = 0;

      carousel.addEventListener('mousedown', (e) => {
        mouseDown = true;
        mouseStartX = e.clientX;
        carousel.classList.add('swiping');
      });

      carousel.addEventListener('mouseleave', () => {
        if (mouseDown) {
          mouseDown = false;
          carousel.classList.remove('swiping');
        }
      });

      carousel.addEventListener('mouseup', (e) => {
        if (!mouseDown) return;
        mouseDown = false;
        carousel.classList.remove('swiping');
        const dx = e.clientX - mouseStartX;
        if (Math.abs(dx) > 40) {
          dx > 0 ? goPrev() : goNext();
        }
      });

      // Keyboard
      carousel.setAttribute('tabindex', '0');
      carousel.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft') { e.preventDefault(); goPrev(); }
        if (e.key === 'ArrowRight') { e.preventDefault(); goNext(); }
      });
    } else {
      // Single slide: hide nav
      prevBtn.style.display = 'none';
      nextBtn.style.display = 'none';
    }
  });
}

/* ============================================================
   Custom Language Switcher (Google Translate via hash)
   ============================================================ */
(function() {
  var select = document.getElementById('lang-switcher');
  if (!select) return;

  // Detect current language from URL hash
  function getCurrentLang() {
    var m = window.location.hash.match(/googtrans\(en\|([a-z-]+)\)/);
    return m ? m[1] : 'en';
  }

  // Show currently active language in dropdown
  var current = getCurrentLang();
  if (current && select.querySelector('option[value="' + current + '"]')) {
    select.value = current;
  }

  select.addEventListener('change', function() {
    var lang = this.value;
    if (lang === 'en') {
      // Reset: clear cookie, remove hash, reload to plain English
      document.cookie = 'googtrans=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/;';
      window.location.href = window.location.pathname;
    } else {
      // Google's native mechanism: #googtrans(en|LANG) triggers translation on page load
      window.location.href = window.location.pathname + '#googtrans(en|' + lang + ')';
    }
  });
})();
