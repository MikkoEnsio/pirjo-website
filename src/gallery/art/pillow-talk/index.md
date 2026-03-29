---
title: Pillow Talk Exhibition
layout: base.njk
---
# Pillow Talk Exhibition

<div class="gallery-grid">
  <a href="#" onclick="openLightbox(0); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/pillow-talk/2015-05-26-pillow-talk-aamulla1-1.jpg" alt="2015 05 26 pillow talk aamulla1 1"></a>
  <a href="#" onclick="openLightbox(1); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/pillow-talk/2015-06-05-12.19.59.jpg" alt="2015 06 05 12.19.59"></a>
  <a href="#" onclick="openLightbox(2); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/pillow-talk/2015-06-05-12.21.03.jpg" alt="2015 06 05 12.21.03"></a>
  <a href="#" onclick="openLightbox(3); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/pillow-talk/book-of-dreams.jpg" alt="book of dreams"></a>
  <a href="#" onclick="openLightbox(4); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/pillow-talk/dirty-dozen-7.jpg" alt="dirty dozen 7"></a>
  <a href="#" onclick="openLightbox(5); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/pillow-talk/dreams.jpg" alt="dreams"></a>
  <a href="#" onclick="openLightbox(6); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/pillow-talk/img_20150526_114253.jpg" alt="img 20150526 114253"></a>
  <a href="#" onclick="openLightbox(7); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/pillow-talk/pillow-talk-exhibition.jpg" alt="pillow talk exhibition"></a>
  <a href="#" onclick="openLightbox(8); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/pillow-talk/sina_ja_minadsc02189.jpg" alt="sina ja minadsc02189"></a>
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
    "/assets/images/art/pillow-talk/2015-05-26-pillow-talk-aamulla1-1.jpg",
    "/assets/images/art/pillow-talk/2015-06-05-12.19.59.jpg",
    "/assets/images/art/pillow-talk/2015-06-05-12.21.03.jpg",
    "/assets/images/art/pillow-talk/book-of-dreams.jpg",
    "/assets/images/art/pillow-talk/dirty-dozen-7.jpg",
    "/assets/images/art/pillow-talk/dreams.jpg",
    "/assets/images/art/pillow-talk/img_20150526_114253.jpg",
    "/assets/images/art/pillow-talk/pillow-talk-exhibition.jpg",
    "/assets/images/art/pillow-talk/sina_ja_minadsc02189.jpg"
  ];
  const galleryTitles = [
    "2015 05 26 pillow talk aamulla1 1",
    "2015 06 05 12.19.59",
    "2015 06 05 12.21.03",
    "book of dreams",
    "dirty dozen 7",
    "dreams",
    "img 20150526 114253",
    "pillow talk exhibition",
    "sina ja minadsc02189"
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
