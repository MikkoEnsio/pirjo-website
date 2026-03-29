---
title: Useless Things!?
layout: base.njk
---
# Useless Things!?

<div class="gallery-grid">
  <a href="#" onclick="openLightbox(0); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/useless-things/17.mummon-laukku-tarpeetontatavaraa-.jpg" alt="17.mummon laukku tarpeetontatavaraa "></a>
  <a href="#" onclick="openLightbox(1); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/useless-things/3.alchemytarpeetontatavaraa-.jpg" alt="3.alchemytarpeetontatavaraa "></a>
  <a href="#" onclick="openLightbox(2); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/useless-things/4.auringonlaskutarpeetontatavaraa-.jpg" alt="4.auringonlaskutarpeetontatavaraa "></a>
  <a href="#" onclick="openLightbox(3); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/useless-things/6.siivilatarpeetontatavaraa-.jpg" alt="6.siivilatarpeetontatavaraa "></a>
  <a href="#" onclick="openLightbox(4); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/useless-things/aurinko.jpg" alt="aurinko"></a>
  <a href="#" onclick="openLightbox(5); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/useless-things/japonese.jpg" alt="japonese"></a>
  <a href="#" onclick="openLightbox(6); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/useless-things/ok.-1.jpg" alt="ok. 1"></a>
  <a href="#" onclick="openLightbox(7); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/useless-things/p7295177.jpg" alt="p7295177"></a>
  <a href="#" onclick="openLightbox(8); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/useless-things/stack.jpg" alt="stack"></a>
  <a href="#" onclick="openLightbox(9); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/useless-things/the-end.jpg" alt="the end"></a>
</div>

<div id="lightbox" class="lightbox" onclick="lightboxBackgroundClick(event)">
  <button type="button" class="lightbox-close" onclick="closeLightbox(event)">×</button>
  <button type="button" class="lightbox-prev" onclick="prevImage(event)">‹</button>
  <div class="lightbox-content" onclick="event.stopPropagation()">
    <img id="lightbox-image" class="lightbox-image" src="" alt="">
    <div id="lightbox-caption" class="lightbox-caption"></div>
  </div>
  <button type="button" class="lightbox-next" onclick="nextImage(event)">›</button>
</div>

<script>
  const galleryImages = [
    "/assets/images/art/useless-things/17.mummon-laukku-tarpeetontatavaraa-.jpg",
    "/assets/images/art/useless-things/3.alchemytarpeetontatavaraa-.jpg",
    "/assets/images/art/useless-things/4.auringonlaskutarpeetontatavaraa-.jpg",
    "/assets/images/art/useless-things/6.siivilatarpeetontatavaraa-.jpg",
    "/assets/images/art/useless-things/aurinko.jpg",
    "/assets/images/art/useless-things/japonese.jpg",
    "/assets/images/art/useless-things/ok.-1.jpg",
    "/assets/images/art/useless-things/p7295177.jpg",
    "/assets/images/art/useless-things/stack.jpg",
    "/assets/images/art/useless-things/the-end.jpg"
  ];
  const galleryTitles = [
    "17.mummon laukku tarpeetontatavaraa ",
    "3.alchemytarpeetontatavaraa ",
    "4.auringonlaskutarpeetontatavaraa ",
    "6.siivilatarpeetontatavaraa ",
    "aurinko",
    "japonese",
    "ok. 1",
    "p7295177",
    "stack",
    "the end"
  ];
  let currentImageIndex = 0;
  function updateLightbox() {
    document.getElementById("lightbox-image").src = galleryImages[currentImageIndex];
    document.getElementById("lightbox-image").alt = galleryTitles[currentImageIndex];
    document.getElementById("lightbox-caption").textContent = galleryTitles[currentImageIndex];
  }
  function openLightbox(index) {
    currentImageIndex = index;
    updateLightbox();
    document.getElementById("lightbox").style.display = "flex";
  }
  function closeLightbox(event) {
    if (event) event.stopPropagation();
    document.getElementById("lightbox").style.display = "none";
  }
  function prevImage(event) {
    event.stopPropagation();
    currentImageIndex = (currentImageIndex - 1 + galleryImages.length) % galleryImages.length;
    updateLightbox();
  }
  function nextImage(event) {
    event.stopPropagation();
    currentImageIndex = (currentImageIndex + 1) % galleryImages.length;
    updateLightbox();
  }
  function lightboxBackgroundClick(event) {
    if (event.target.id === "lightbox") closeLightbox();
  }
  document.addEventListener("keydown", function(event) {
    const lightbox = document.getElementById("lightbox");
    if (lightbox.style.display !== "flex") return;
    if (event.key === "Escape") closeLightbox();
    if (event.key === "ArrowLeft") { currentImageIndex = (currentImageIndex - 1 + galleryImages.length) % galleryImages.length; updateLightbox(); }
    if (event.key === "ArrowRight") { currentImageIndex = (currentImageIndex + 1) % galleryImages.length; updateLightbox(); }
  });
</script>
