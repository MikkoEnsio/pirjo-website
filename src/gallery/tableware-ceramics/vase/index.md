---
title: Vase
layout: base.njk
---
# Vase

<div class="gallery-grid">
  <a href="#" onclick="openLightbox(0); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/vase/2015-06-12-14.49.11-2.jpg" alt="2015 06 12 14.49.11 2"></a>
  <a href="#" onclick="openLightbox(1); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/vase/20160525_153123.jpg" alt="20160525 153123"></a>
  <a href="#" onclick="openLightbox(2); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/vase/20160610_134248.jpg" alt="20160610 134248"></a>
  <a href="#" onclick="openLightbox(3); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/vase/2017-09-21_vihrea_valumaljakko.jpg" alt="2017 09 21 vihrea valumaljakko"></a>
  <a href="#" onclick="openLightbox(4); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/vase/img_20191105_153817_001.jpg" alt="img 20191105 153817 001"></a>
  <a href="#" onclick="openLightbox(5); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/vase/pallomaljakkopilkkukorkeak2_edited.jpg" alt="pallomaljakkopilkkukorkeak2 edited"></a>
  <a href="#" onclick="openLightbox(6); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/vase/pilkullisia-maljakoita.jpg" alt="pilkullisia maljakoita"></a>
  <a href="#" onclick="openLightbox(7); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/vase/syreenit-pirjonmaljakossa-3.jpg" alt="syreenit pirjonmaljakossa 3"></a>
  <a href="#" onclick="openLightbox(8); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/vase/valetut-maljakot-kopio2.jpg" alt="valetut maljakot kopio2"></a>
  <a href="#" onclick="openLightbox(9); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/vase/valumaljakkoturkoosi.jpg" alt="valumaljakkoturkoosi"></a>
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
    "/assets/images/tableware-ceramics/vase/2015-06-12-14.49.11-2.jpg",
    "/assets/images/tableware-ceramics/vase/20160525_153123.jpg",
    "/assets/images/tableware-ceramics/vase/20160610_134248.jpg",
    "/assets/images/tableware-ceramics/vase/2017-09-21_vihrea_valumaljakko.jpg",
    "/assets/images/tableware-ceramics/vase/img_20191105_153817_001.jpg",
    "/assets/images/tableware-ceramics/vase/pallomaljakkopilkkukorkeak2_edited.jpg",
    "/assets/images/tableware-ceramics/vase/pilkullisia-maljakoita.jpg",
    "/assets/images/tableware-ceramics/vase/syreenit-pirjonmaljakossa-3.jpg",
    "/assets/images/tableware-ceramics/vase/valetut-maljakot-kopio2.jpg",
    "/assets/images/tableware-ceramics/vase/valumaljakkoturkoosi.jpg"
  ];
  const galleryTitles = [
    "2015 06 12 14.49.11 2",
    "20160525 153123",
    "20160610 134248",
    "2017 09 21 vihrea valumaljakko",
    "img 20191105 153817 001",
    "pallomaljakkopilkkukorkeak2 edited",
    "pilkullisia maljakoita",
    "syreenit pirjonmaljakossa 3",
    "valetut maljakot kopio2",
    "valumaljakkoturkoosi"
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
