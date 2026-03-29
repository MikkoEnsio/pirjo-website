---
title: Invisible Moments Exhibition
layout: base.njk
---
# Invisible Moments Exhibition

<div class="gallery-grid">
  <a href="#" onclick="openLightbox(0); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/20240924_170007-02x-kopio.jpg" alt="20240924 170007 02x kopio"></a>
  <a href="#" onclick="openLightbox(1); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/20240924_174916-02x.jpg" alt="20240924 174916 02x"></a>
  <a href="#" onclick="openLightbox(2); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/20241109_120122-03x-kopio.jpg" alt="20241109 120122 03x kopio"></a>
  <a href="#" onclick="openLightbox(3); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/20241109_120433-02x-kopio.jpg" alt="20241109 120433 02x kopio"></a>
  <a href="#" onclick="openLightbox(4); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/20241109_120515-02x-kopio.jpg" alt="20241109 120515 02x kopio"></a>
  <a href="#" onclick="openLightbox(5); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/20241109_120548-02x-kopio_edited.jpg" alt="20241109 120548 02x kopio edited"></a>
  <a href="#" onclick="openLightbox(6); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/20241109_120607-02x-kopio.jpg" alt="20241109 120607 02x kopio"></a>
  <a href="#" onclick="openLightbox(7); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/20241109_120628-02x-kopio.jpg" alt="20241109 120628 02x kopio"></a>
  <a href="#" onclick="openLightbox(8); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/20241109_120640-02xkopio.jpg" alt="20241109 120640 02xkopio"></a>
  <a href="#" onclick="openLightbox(9); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/20241109_120659-01-02xkopio.jpg" alt="20241109 120659 01 02xkopio"></a>
  <a href="#" onclick="openLightbox(10); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/20241109_120707-01-kopio.jpeg" alt="20241109 120707 01 kopio"></a>
  <a href="#" onclick="openLightbox(11); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/20241109_120724-02x-kopio.jpg" alt="20241109 120724 02x kopio"></a>
  <a href="#" onclick="openLightbox(12); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/20241109_120747-02x.jpg" alt="20241109 120747 02x"></a>
  <a href="#" onclick="openLightbox(13); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/20241109_120758-02x-kopio.jpg" alt="20241109 120758 02x kopio"></a>
  <a href="#" onclick="openLightbox(14); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/20241109_120834-02x-kopio.jpg" alt="20241109 120834 02x kopio"></a>
  <a href="#" onclick="openLightbox(15); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/dsc01260-kopio-2.jpg" alt="dsc01260 kopio 2"></a>
  <a href="#" onclick="openLightbox(16); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/dsc02284-yhdistelma-kopio.jpg" alt="dsc02284 yhdistelma kopio"></a>
  <a href="#" onclick="openLightbox(17); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/pirjopesonepriitkoiv.jpg" alt="pirjopesonepriitkoiv"></a>
  <a href="#" onclick="openLightbox(18); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/x20240807_074617-01-kopio.jpeg" alt="x20240807 074617 01 kopio"></a>
  <a href="#" onclick="openLightbox(19); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/invisible-moments/xdsc08919-kopio.jpg" alt="xdsc08919 kopio"></a>
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
    "/assets/images/art/invisible-moments/20240924_170007-02x-kopio.jpg",
    "/assets/images/art/invisible-moments/20240924_174916-02x.jpg",
    "/assets/images/art/invisible-moments/20241109_120122-03x-kopio.jpg",
    "/assets/images/art/invisible-moments/20241109_120433-02x-kopio.jpg",
    "/assets/images/art/invisible-moments/20241109_120515-02x-kopio.jpg",
    "/assets/images/art/invisible-moments/20241109_120548-02x-kopio_edited.jpg",
    "/assets/images/art/invisible-moments/20241109_120607-02x-kopio.jpg",
    "/assets/images/art/invisible-moments/20241109_120628-02x-kopio.jpg",
    "/assets/images/art/invisible-moments/20241109_120640-02xkopio.jpg",
    "/assets/images/art/invisible-moments/20241109_120659-01-02xkopio.jpg",
    "/assets/images/art/invisible-moments/20241109_120707-01-kopio.jpeg",
    "/assets/images/art/invisible-moments/20241109_120724-02x-kopio.jpg",
    "/assets/images/art/invisible-moments/20241109_120747-02x.jpg",
    "/assets/images/art/invisible-moments/20241109_120758-02x-kopio.jpg",
    "/assets/images/art/invisible-moments/20241109_120834-02x-kopio.jpg",
    "/assets/images/art/invisible-moments/dsc01260-kopio-2.jpg",
    "/assets/images/art/invisible-moments/dsc02284-yhdistelma-kopio.jpg",
    "/assets/images/art/invisible-moments/pirjopesonepriitkoiv.jpg",
    "/assets/images/art/invisible-moments/x20240807_074617-01-kopio.jpeg",
    "/assets/images/art/invisible-moments/xdsc08919-kopio.jpg"
  ];
  const galleryTitles = [
    "20240924 170007 02x kopio",
    "20240924 174916 02x",
    "20241109 120122 03x kopio",
    "20241109 120433 02x kopio",
    "20241109 120515 02x kopio",
    "20241109 120548 02x kopio edited",
    "20241109 120607 02x kopio",
    "20241109 120628 02x kopio",
    "20241109 120640 02xkopio",
    "20241109 120659 01 02xkopio",
    "20241109 120707 01 kopio",
    "20241109 120724 02x kopio",
    "20241109 120747 02x",
    "20241109 120758 02x kopio",
    "20241109 120834 02x kopio",
    "dsc01260 kopio 2",
    "dsc02284 yhdistelma kopio",
    "pirjopesonepriitkoiv",
    "x20240807 074617 01 kopio",
    "xdsc08919 kopio"
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
