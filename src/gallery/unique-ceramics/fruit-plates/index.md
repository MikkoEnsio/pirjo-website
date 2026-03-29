---
title: Fruit Plates
layout: base.njk
---
# Fruit Plates

<div class="gallery-grid">
  <a href="#" onclick="openLightbox(0); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/fruit-plates/37.keramiikkaapienessatilassadesignforumshowroom-vadit2015.jpg" alt="37.keramiikkaapienessatilassadesignforumshowroom vadit2015"></a>
  <a href="#" onclick="openLightbox(1); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/fruit-plates/detail-of-plate.jpg" alt="detail of plate"></a>
  <a href="#" onclick="openLightbox(2); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/fruit-plates/plate.jpg" alt="plate"></a>
  <a href="#" onclick="openLightbox(3); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/fruit-plates/puzzle-plate.jpg" alt="puzzle plate"></a>
  <a href="#" onclick="openLightbox(4); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/fruit-plates/reikavati--ovaali-vihrea-ja-kukka.jpg" alt="reikavati  ovaali vihrea ja kukka"></a>
  <a href="#" onclick="openLightbox(5); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/fruit-plates/reikavati--vinonelio-turkoosi-.jpg" alt="reikavati  vinonelio turkoosi "></a>
  <a href="#" onclick="openLightbox(6); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/fruit-plates/reikavati-palapeli-musta-001-6.jpg" alt="reikavati palapeli musta 001 6"></a>
  <a href="#" onclick="openLightbox(7); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/fruit-plates/reikavati-palapeli-musta-5-013.jpg" alt="reikavati palapeli musta 5 013"></a>
  <a href="#" onclick="openLightbox(8); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/fruit-plates/reikavati-solu-vihrea-jpg.jpg" alt="reikavati solu vihrea jpg"></a>
  <a href="#" onclick="openLightbox(9); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/fruit-plates/reikavati-tahti-violetti012.jpg" alt="reikavati tahti violetti012"></a>
  <a href="#" onclick="openLightbox(10); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/fruit-plates/reikavatiympyrat-keltainen-.jpg" alt="reikavatiympyrat keltainen "></a>
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
    "/assets/images/unique-ceramics/fruit-plates/37.keramiikkaapienessatilassadesignforumshowroom-vadit2015.jpg",
    "/assets/images/unique-ceramics/fruit-plates/detail-of-plate.jpg",
    "/assets/images/unique-ceramics/fruit-plates/plate.jpg",
    "/assets/images/unique-ceramics/fruit-plates/puzzle-plate.jpg",
    "/assets/images/unique-ceramics/fruit-plates/reikavati--ovaali-vihrea-ja-kukka.jpg",
    "/assets/images/unique-ceramics/fruit-plates/reikavati--vinonelio-turkoosi-.jpg",
    "/assets/images/unique-ceramics/fruit-plates/reikavati-palapeli-musta-001-6.jpg",
    "/assets/images/unique-ceramics/fruit-plates/reikavati-palapeli-musta-5-013.jpg",
    "/assets/images/unique-ceramics/fruit-plates/reikavati-solu-vihrea-jpg.jpg",
    "/assets/images/unique-ceramics/fruit-plates/reikavati-tahti-violetti012.jpg",
    "/assets/images/unique-ceramics/fruit-plates/reikavatiympyrat-keltainen-.jpg"
  ];
  const galleryTitles = [
    "37.keramiikkaapienessatilassadesignforumshowroom vadit2015",
    "detail of plate",
    "plate",
    "puzzle plate",
    "reikavati  ovaali vihrea ja kukka",
    "reikavati  vinonelio turkoosi ",
    "reikavati palapeli musta 001 6",
    "reikavati palapeli musta 5 013",
    "reikavati solu vihrea jpg",
    "reikavati tahti violetti012",
    "reikavatiympyrat keltainen "
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
