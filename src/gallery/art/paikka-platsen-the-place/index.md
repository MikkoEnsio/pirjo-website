---
title: Paikka-Platsen-The Place, Suomenlinna
layout: base.njk
---
# Paikka-Platsen-The Place, Suomenlinna

<div class="gallery-grid">
  <a href="#" onclick="openLightbox(0); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/paikka-platsen-the-place/20220727_114956cropattu.jpg" alt="20220727 114956cropattu"></a>
  <a href="#" onclick="openLightbox(1); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/paikka-platsen-the-place/20220816_173556cropattu.jpg" alt="20220816 173556cropattu"></a>
  <a href="#" onclick="openLightbox(2); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/paikka-platsen-the-place/20220819_080118-1.jpg" alt="20220819 080118 1"></a>
  <a href="#" onclick="openLightbox(3); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/paikka-platsen-the-place/clothes-line-.jpeg" alt="clothes line "></a>
  <a href="#" onclick="openLightbox(4); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/paikka-platsen-the-place/collage1.jpg" alt="collage1"></a>
  <a href="#" onclick="openLightbox(5); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/paikka-platsen-the-place/collage2.jpg" alt="collage2"></a>
  <a href="#" onclick="openLightbox(6); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/paikka-platsen-the-place/detail1.jpg" alt="detail1"></a>
  <a href="#" onclick="openLightbox(7); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/paikka-platsen-the-place/detail2jpg.jpg" alt="detail2jpg"></a>
  <a href="#" onclick="openLightbox(8); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/paikka-platsen-the-place/detail3jpg.jpg" alt="detail3jpg"></a>
  <a href="#" onclick="openLightbox(9); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/paikka-platsen-the-place/detail4.jpg" alt="detail4"></a>
  <a href="#" onclick="openLightbox(10); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/paikka-platsen-the-place/detail5.jpg" alt="detail5"></a>
  <a href="#" onclick="openLightbox(11); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/paikka-platsen-the-place/paikka-relief1.jpg" alt="paikka relief1"></a>
  <a href="#" onclick="openLightbox(12); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/paikka-platsen-the-place/paikka-relief2.jpg" alt="paikka relief2"></a>
  <a href="#" onclick="openLightbox(13); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/paikka-platsen-the-place/paikka-relief3.jpg" alt="paikka relief3"></a>
  <a href="#" onclick="openLightbox(14); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/paikka-platsen-the-place/paikka-reliefes.jpg" alt="paikka reliefes"></a>
  <a href="#" onclick="openLightbox(15); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/paikka-platsen-the-place/paikka-reliefes2.jpg" alt="paikka reliefes2"></a>
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
    "/assets/images/art/paikka-platsen-the-place/20220727_114956cropattu.jpg",
    "/assets/images/art/paikka-platsen-the-place/20220816_173556cropattu.jpg",
    "/assets/images/art/paikka-platsen-the-place/20220819_080118-1.jpg",
    "/assets/images/art/paikka-platsen-the-place/clothes-line-.jpeg",
    "/assets/images/art/paikka-platsen-the-place/collage1.jpg",
    "/assets/images/art/paikka-platsen-the-place/collage2.jpg",
    "/assets/images/art/paikka-platsen-the-place/detail1.jpg",
    "/assets/images/art/paikka-platsen-the-place/detail2jpg.jpg",
    "/assets/images/art/paikka-platsen-the-place/detail3jpg.jpg",
    "/assets/images/art/paikka-platsen-the-place/detail4.jpg",
    "/assets/images/art/paikka-platsen-the-place/detail5.jpg",
    "/assets/images/art/paikka-platsen-the-place/paikka-relief1.jpg",
    "/assets/images/art/paikka-platsen-the-place/paikka-relief2.jpg",
    "/assets/images/art/paikka-platsen-the-place/paikka-relief3.jpg",
    "/assets/images/art/paikka-platsen-the-place/paikka-reliefes.jpg",
    "/assets/images/art/paikka-platsen-the-place/paikka-reliefes2.jpg"
  ];
  const galleryTitles = [
    "20220727 114956cropattu",
    "20220816 173556cropattu",
    "20220819 080118 1",
    "clothes line ",
    "collage1",
    "collage2",
    "detail1",
    "detail2jpg",
    "detail3jpg",
    "detail4",
    "detail5",
    "paikka relief1",
    "paikka relief2",
    "paikka relief3",
    "paikka reliefes",
    "paikka reliefes2"
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
