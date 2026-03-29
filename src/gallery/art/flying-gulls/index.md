---
title: Flying Gulls
layout: base.njk
---
# Flying Gulls

<div class="gallery-grid">
  <a href="#" onclick="openLightbox(0); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/flying-gulls/2014-10-17-11.50.51.jpg" alt="2014 10 17 11.50.51"></a>
  <a href="#" onclick="openLightbox(1); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/flying-gulls/2016-03-29-15.04.21.jpg" alt="2016 03 29 15.04.21"></a>
  <a href="#" onclick="openLightbox(2); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/flying-gulls/dsc02282.jpg" alt="dsc02282"></a>
  <a href="#" onclick="openLightbox(3); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/flying-gulls/lentavat_lokit_pirjo_pesonen__.jpg" alt="lentavat lokit pirjo pesonen  "></a>
  <a href="#" onclick="openLightbox(4); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/flying-gulls/nakyma-potista.jpg" alt="nakyma potista"></a>
  <a href="#" onclick="openLightbox(5); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/flying-gulls/suomenlinna-.jpg" alt="suomenlinna "></a>
  <a href="#" onclick="openLightbox(6); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/flying-gulls/waiting.jpg" alt="waiting"></a>
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
    "/assets/images/art/flying-gulls/2014-10-17-11.50.51.jpg",
    "/assets/images/art/flying-gulls/2016-03-29-15.04.21.jpg",
    "/assets/images/art/flying-gulls/dsc02282.jpg",
    "/assets/images/art/flying-gulls/lentavat_lokit_pirjo_pesonen__.jpg",
    "/assets/images/art/flying-gulls/nakyma-potista.jpg",
    "/assets/images/art/flying-gulls/suomenlinna-.jpg",
    "/assets/images/art/flying-gulls/waiting.jpg"
  ];
  const galleryTitles = [
    "2014 10 17 11.50.51",
    "2016 03 29 15.04.21",
    "dsc02282",
    "lentavat lokit pirjo pesonen  ",
    "nakyma potista",
    "suomenlinna ",
    "waiting"
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
