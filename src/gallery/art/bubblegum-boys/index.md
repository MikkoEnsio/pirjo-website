---
title: Bubblegum Boys
layout: base.njk
---
# Bubblegum Boys

<div class="gallery-grid">
  <a href="#" onclick="openLightbox(0); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/bubblegum-boys/20190513_142215-1.jpg" alt="20190513 142215 1"></a>
  <a href="#" onclick="openLightbox(1); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/bubblegum-boys/20190627bubblegum-boy-3.jpg" alt="20190627bubblegum boy 3"></a>
  <a href="#" onclick="openLightbox(2); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/bubblegum-boys/bubblegum-boy-1.jpg" alt="bubblegum boy 1"></a>
  <a href="#" onclick="openLightbox(3); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/bubblegum-boys/bubblegum2520boys2520serie_edited_edited.png" alt="bubblegum2520boys2520serie edited edited"></a>
  <a href="#" onclick="openLightbox(4); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/bubblegum-boys/bubblegumboy2-1.jpg" alt="bubblegumboy2 1"></a>
  <a href="#" onclick="openLightbox(5); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/bubblegum-boys/purkkapoika2bubblegumboy2-.jpg" alt="purkkapoika2bubblegumboy2 "></a>
  <a href="#" onclick="openLightbox(6); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/bubblegum-boys/purkkapoika3-bubblegumboy3-.jpg" alt="purkkapoika3 bubblegumboy3 "></a>
  <a href="#" onclick="openLightbox(7); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/bubblegum-boys/purkkapoika3.jpg" alt="purkkapoika3"></a>
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
    "/assets/images/art/bubblegum-boys/20190513_142215-1.jpg",
    "/assets/images/art/bubblegum-boys/20190627bubblegum-boy-3.jpg",
    "/assets/images/art/bubblegum-boys/bubblegum-boy-1.jpg",
    "/assets/images/art/bubblegum-boys/bubblegum2520boys2520serie_edited_edited.png",
    "/assets/images/art/bubblegum-boys/bubblegumboy2-1.jpg",
    "/assets/images/art/bubblegum-boys/purkkapoika2bubblegumboy2-.jpg",
    "/assets/images/art/bubblegum-boys/purkkapoika3-bubblegumboy3-.jpg",
    "/assets/images/art/bubblegum-boys/purkkapoika3.jpg"
  ];
  const galleryTitles = [
    "20190513 142215 1",
    "20190627bubblegum boy 3",
    "bubblegum boy 1",
    "bubblegum2520boys2520serie edited edited",
    "bubblegumboy2 1",
    "purkkapoika2bubblegumboy2 ",
    "purkkapoika3 bubblegumboy3 ",
    "purkkapoika3"
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
