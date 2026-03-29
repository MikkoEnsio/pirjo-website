---
title: Small Bowls
layout: base.njk
---
# Small Bowls

<div class="gallery-grid">
  <a href="#" onclick="openLightbox(0); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/small-bowls/2015-06-12-karpasia-kulhossa_1.jpg" alt="2015 06 12 karpasia kulhossa 1"></a>
  <a href="#" onclick="openLightbox(1); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/small-bowls/20160425_115354.jpg" alt="20160425 115354"></a>
  <a href="#" onclick="openLightbox(2); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/small-bowls/2018-09-24-15.34.41.jpg" alt="2018 09 24 15.34.41"></a>
  <a href="#" onclick="openLightbox(3); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/small-bowls/detail-fly-bowl.jpg" alt="detail fly bowl"></a>
  <a href="#" onclick="openLightbox(4); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/small-bowls/img_0148-kopio.jpg" alt="img 0148 kopio"></a>
  <a href="#" onclick="openLightbox(5); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/small-bowls/small-bowls.jpg" alt="small bowls"></a>
  <a href="#" onclick="openLightbox(6); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/small-bowls/tea-for-two3kopio--1_edited.jpg" alt="tea for two3kopio  1 edited"></a>
  <a href="#" onclick="openLightbox(7); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/small-bowls/vihreat-pikkukulhot.jpg" alt="vihreat pikkukulhot"></a>
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
    "/assets/images/tableware-ceramics/small-bowls/2015-06-12-karpasia-kulhossa_1.jpg",
    "/assets/images/tableware-ceramics/small-bowls/20160425_115354.jpg",
    "/assets/images/tableware-ceramics/small-bowls/2018-09-24-15.34.41.jpg",
    "/assets/images/tableware-ceramics/small-bowls/detail-fly-bowl.jpg",
    "/assets/images/tableware-ceramics/small-bowls/img_0148-kopio.jpg",
    "/assets/images/tableware-ceramics/small-bowls/small-bowls.jpg",
    "/assets/images/tableware-ceramics/small-bowls/tea-for-two3kopio--1_edited.jpg",
    "/assets/images/tableware-ceramics/small-bowls/vihreat-pikkukulhot.jpg"
  ];
  const galleryTitles = [
    "2015 06 12 karpasia kulhossa 1",
    "20160425 115354",
    "2018 09 24 15.34.41",
    "detail fly bowl",
    "img 0148 kopio",
    "small bowls",
    "tea for two3kopio  1 edited",
    "vihreat pikkukulhot"
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
