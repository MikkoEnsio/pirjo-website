---
title: Pure Misery Exhibition
layout: base.njk
---
# Pure Misery Exhibition

<div class="gallery-grid">
  <a href="#" onclick="openLightbox(0); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/pure-misery/hui_kauhistus_valmis_tyo_019-1.jpg" alt="hui kauhistus valmis tyo 019 1"></a>
  <a href="#" onclick="openLightbox(1); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/pure-misery/katselen-nuoria-naisia-galleriassa2-kropattu-07-016.jpg" alt="katselen nuoria naisia galleriassa2 kropattu 07 016"></a>
  <a href="#" onclick="openLightbox(2); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/pure-misery/kauniita-unia008-9.jpg" alt="kauniita unia008 9"></a>
  <a href="#" onclick="openLightbox(3); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/pure-misery/kuumat-aallot-valmis-teos-036-1.jpg" alt="kuumat aallot valmis teos 036 1"></a>
  <a href="#" onclick="openLightbox(4); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/pure-misery/pure-misery-exhibition.jpg" alt="pure misery exhibition"></a>
  <a href="#" onclick="openLightbox(5); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/pure-misery/state-of-mind-boxes-031.jpg" alt="state of mind boxes 031"></a>
  <a href="#" onclick="openLightbox(6); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/pure-misery/tunnen-itseni-paksuksi-016-.jpg" alt="tunnen itseni paksuksi 016 "></a>
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
    "/assets/images/art/pure-misery/hui_kauhistus_valmis_tyo_019-1.jpg",
    "/assets/images/art/pure-misery/katselen-nuoria-naisia-galleriassa2-kropattu-07-016.jpg",
    "/assets/images/art/pure-misery/kauniita-unia008-9.jpg",
    "/assets/images/art/pure-misery/kuumat-aallot-valmis-teos-036-1.jpg",
    "/assets/images/art/pure-misery/pure-misery-exhibition.jpg",
    "/assets/images/art/pure-misery/state-of-mind-boxes-031.jpg",
    "/assets/images/art/pure-misery/tunnen-itseni-paksuksi-016-.jpg"
  ];
  const galleryTitles = [
    "hui kauhistus valmis tyo 019 1",
    "katselen nuoria naisia galleriassa2 kropattu 07 016",
    "kauniita unia008 9",
    "kuumat aallot valmis teos 036 1",
    "pure misery exhibition",
    "state of mind boxes 031",
    "tunnen itseni paksuksi 016 "
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
