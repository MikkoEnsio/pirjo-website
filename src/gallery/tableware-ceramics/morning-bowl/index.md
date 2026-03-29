---
title: Morning Bowl
layout: base.njk
---
# Morning Bowl

<div class="gallery-grid">
  <a href="#" onclick="openLightbox(0); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/morning-bowl/20200414_171100.jpg" alt="20200414 171100"></a>
  <a href="#" onclick="openLightbox(1); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/morning-bowl/20200512_175612.jpg" alt="20200512 175612"></a>
  <a href="#" onclick="openLightbox(2); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/morning-bowl/img_0147.jpg" alt="img 0147"></a>
  <a href="#" onclick="openLightbox(3); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/morning-bowl/img_20200413_094553_692.jpg" alt="img 20200413 094553 692"></a>
  <a href="#" onclick="openLightbox(4); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/morning-bowl/mustat-uurtokulhot-071--1-kopio.jpg" alt="mustat uurtokulhot 071  1 kopio"></a>
  <a href="#" onclick="openLightbox(5); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/morning-bowl/small-bowls-1.jpg" alt="small bowls 1"></a>
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
    "/assets/images/tableware-ceramics/morning-bowl/20200414_171100.jpg",
    "/assets/images/tableware-ceramics/morning-bowl/20200512_175612.jpg",
    "/assets/images/tableware-ceramics/morning-bowl/img_0147.jpg",
    "/assets/images/tableware-ceramics/morning-bowl/img_20200413_094553_692.jpg",
    "/assets/images/tableware-ceramics/morning-bowl/mustat-uurtokulhot-071--1-kopio.jpg",
    "/assets/images/tableware-ceramics/morning-bowl/small-bowls-1.jpg"
  ];
  const galleryTitles = [
    "20200414 171100",
    "20200512 175612",
    "img 0147",
    "img 20200413 094553 692",
    "mustat uurtokulhot 071  1 kopio",
    "small bowls 1"
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
