---
title: At the Factory
layout: base.njk
---
# At the Factory

<div class="gallery-grid">
  <a href="#" onclick="openLightbox(0); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/at-the-factory/back-to-u.s.s.r3-kopio_edited.jpg" alt="back to u.s.s.r3 kopio edited"></a>
  <a href="#" onclick="openLightbox(1); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/at-the-factory/jars.jpg" alt="jars"></a>
  <a href="#" onclick="openLightbox(2); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/at-the-factory/machine1.jpg" alt="machine1"></a>
  <a href="#" onclick="openLightbox(3); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/at-the-factory/machine2_edited.jpg" alt="machine2 edited"></a>
  <a href="#" onclick="openLightbox(4); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/at-the-factory/pesonen-.jpg" alt="pesonen "></a>
  <a href="#" onclick="openLightbox(5); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/at-the-factory/pesonenprosessi-osa-.jpg" alt="pesonenprosessi osa "></a>
  <a href="#" onclick="openLightbox(6); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/at-the-factory/put-put.jpg" alt="put put"></a>
  <a href="#" onclick="openLightbox(7); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/at-the-factory/tehtaalla_.jpg" alt="tehtaalla "></a>
  <a href="#" onclick="openLightbox(8); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/at-the-factory/vinkisin-vonksin.jpg" alt="vinkisin vonksin"></a>
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
    "/assets/images/art/at-the-factory/back-to-u.s.s.r3-kopio_edited.jpg",
    "/assets/images/art/at-the-factory/jars.jpg",
    "/assets/images/art/at-the-factory/machine1.jpg",
    "/assets/images/art/at-the-factory/machine2_edited.jpg",
    "/assets/images/art/at-the-factory/pesonen-.jpg",
    "/assets/images/art/at-the-factory/pesonenprosessi-osa-.jpg",
    "/assets/images/art/at-the-factory/put-put.jpg",
    "/assets/images/art/at-the-factory/tehtaalla_.jpg",
    "/assets/images/art/at-the-factory/vinkisin-vonksin.jpg"
  ];
  const galleryTitles = [
    "back to u.s.s.r3 kopio edited",
    "jars",
    "machine1",
    "machine2 edited",
    "pesonen ",
    "pesonenprosessi osa ",
    "put put",
    "tehtaalla ",
    "vinkisin vonksin"
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
