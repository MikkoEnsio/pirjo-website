---
title: Dishes and Bowls
layout: base.njk
---
# Dishes and Bowls

<div class="gallery-grid">
  <a href="#" onclick="openLightbox(0); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/dishes-and-bowls/2015-06-12-14.52.59.jpg" alt="2015 06 12 14.52.59"></a>
  <a href="#" onclick="openLightbox(1); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/dishes-and-bowls/2018-09-24-15.34.41.jpg" alt="2018 09 24 15.34.41"></a>
  <a href="#" onclick="openLightbox(2); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/dishes-and-bowls/copy-of-vihrea-kulho4-1.jpg" alt="copy of vihrea kulho4 1"></a>
  <a href="#" onclick="openLightbox(3); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/dishes-and-bowls/punamustat-astiat-kattaus-1.jpg" alt="punamustat astiat kattaus 1"></a>
  <a href="#" onclick="openLightbox(4); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/dishes-and-bowls/punamustat-astiat-kattaus-3.jpg" alt="punamustat astiat kattaus 3"></a>
  <a href="#" onclick="openLightbox(5); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/dishes-and-bowls/uurto-vati.jpg" alt="uurto vati"></a>
  <a href="#" onclick="openLightbox(6); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/dishes-and-bowls/uurtovati-1.jpg" alt="uurtovati 1"></a>
  <a href="#" onclick="openLightbox(7); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/dishes-and-bowls/vekkivatix2.jpg" alt="vekkivatix2"></a>
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
    "/assets/images/tableware-ceramics/dishes-and-bowls/2015-06-12-14.52.59.jpg",
    "/assets/images/tableware-ceramics/dishes-and-bowls/2018-09-24-15.34.41.jpg",
    "/assets/images/tableware-ceramics/dishes-and-bowls/copy-of-vihrea-kulho4-1.jpg",
    "/assets/images/tableware-ceramics/dishes-and-bowls/punamustat-astiat-kattaus-1.jpg",
    "/assets/images/tableware-ceramics/dishes-and-bowls/punamustat-astiat-kattaus-3.jpg",
    "/assets/images/tableware-ceramics/dishes-and-bowls/uurto-vati.jpg",
    "/assets/images/tableware-ceramics/dishes-and-bowls/uurtovati-1.jpg",
    "/assets/images/tableware-ceramics/dishes-and-bowls/vekkivatix2.jpg"
  ];
  const galleryTitles = [
    "2015 06 12 14.52.59",
    "2018 09 24 15.34.41",
    "copy of vihrea kulho4 1",
    "punamustat astiat kattaus 1",
    "punamustat astiat kattaus 3",
    "uurto vati",
    "uurtovati 1",
    "vekkivatix2"
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
