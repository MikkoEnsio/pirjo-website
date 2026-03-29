---
title: Sculptural Vases
layout: base.njk
---
# Sculptural Vases

<div class="gallery-grid">
  <a href="#" onclick="openLightbox(0); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/sculptural-vases/ok.-1.jpg" alt="ok. 1"></a>
  <a href="#" onclick="openLightbox(1); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/sculptural-vases/palkomaljakotpirjo-pesonen_edited.jpg" alt="palkomaljakotpirjo pesonen edited"></a>
  <a href="#" onclick="openLightbox(2); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/sculptural-vases/pallomaljakkopilkkukorkeak2.jpg" alt="pallomaljakkopilkkukorkeak2"></a>
  <a href="#" onclick="openLightbox(3); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/sculptural-vases/tummat-maljakot-3.jpg" alt="tummat maljakot 3"></a>
  <a href="#" onclick="openLightbox(4); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/sculptural-vases/tummat-maljakot-3_edited.jpg" alt="tummat maljakot 3 edited"></a>
  <a href="#" onclick="openLightbox(5); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/sculptural-vases/tummat-maljakot2.jpg" alt="tummat maljakot2"></a>
  <a href="#" onclick="openLightbox(6); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/sculptural-vases/vaalean-siniset-maljakot-.jpg" alt="vaalean siniset maljakot "></a>
  <a href="#" onclick="openLightbox(7); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/sculptural-vases/valetut-maljakot.jpg" alt="valetut maljakot"></a>
  <a href="#" onclick="openLightbox(8); return false;"><img style="object-position: 50% 50%;" src="/assets/images/unique-ceramics/sculptural-vases/vase-hand-built.jpg" alt="vase hand built"></a>
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
    "/assets/images/unique-ceramics/sculptural-vases/ok.-1.jpg",
    "/assets/images/unique-ceramics/sculptural-vases/palkomaljakotpirjo-pesonen_edited.jpg",
    "/assets/images/unique-ceramics/sculptural-vases/pallomaljakkopilkkukorkeak2.jpg",
    "/assets/images/unique-ceramics/sculptural-vases/tummat-maljakot-3.jpg",
    "/assets/images/unique-ceramics/sculptural-vases/tummat-maljakot-3_edited.jpg",
    "/assets/images/unique-ceramics/sculptural-vases/tummat-maljakot2.jpg",
    "/assets/images/unique-ceramics/sculptural-vases/vaalean-siniset-maljakot-.jpg",
    "/assets/images/unique-ceramics/sculptural-vases/valetut-maljakot.jpg",
    "/assets/images/unique-ceramics/sculptural-vases/vase-hand-built.jpg"
  ];
  const galleryTitles = [
    "ok. 1",
    "palkomaljakotpirjo pesonen edited",
    "pallomaljakkopilkkukorkeak2",
    "tummat maljakot 3",
    "tummat maljakot 3 edited",
    "tummat maljakot2",
    "vaalean siniset maljakot ",
    "valetut maljakot",
    "vase hand built"
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
