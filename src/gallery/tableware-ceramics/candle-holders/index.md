---
title: Candle Holders
layout: base.njk
---
# Candle Holders

<div class="gallery-grid">
  <a href="#" onclick="openLightbox(0); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/candle-holders/advent-candle-holder.jpg" alt="advent candle holder"></a>
  <a href="#" onclick="openLightbox(1); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/candle-holders/kynttilanjalkakulho.jpg" alt="kynttilanjalkakulho"></a>
  <a href="#" onclick="openLightbox(2); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/candle-holders/kynttilanjalkakulho1-006.jpg" alt="kynttilanjalkakulho1 006"></a>
  <a href="#" onclick="openLightbox(3); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/candle-holders/turnable-candleholders.jpg" alt="turnable candleholders"></a>
  <a href="#" onclick="openLightbox(4); return false;"><img style="object-position: 50% 50%;" src="/assets/images/tableware-ceramics/candle-holders/valu-kynttilanjalat.jpg" alt="valu kynttilanjalat"></a>
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
    "/assets/images/tableware-ceramics/candle-holders/advent-candle-holder.jpg",
    "/assets/images/tableware-ceramics/candle-holders/kynttilanjalkakulho.jpg",
    "/assets/images/tableware-ceramics/candle-holders/kynttilanjalkakulho1-006.jpg",
    "/assets/images/tableware-ceramics/candle-holders/turnable-candleholders.jpg",
    "/assets/images/tableware-ceramics/candle-holders/valu-kynttilanjalat.jpg"
  ];
  const galleryTitles = [
    "advent candle holder",
    "kynttilanjalkakulho",
    "kynttilanjalkakulho1 006",
    "turnable candleholders",
    "valu kynttilanjalat"
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
