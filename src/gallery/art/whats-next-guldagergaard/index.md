---
title: What's Next? Guldagergaard 2017
layout: base.njk
---
# What's Next? Guldagergaard 2017

<div class="gallery-grid">
  <a href="#" onclick="openLightbox(0); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/whats-next-guldagergaard/52.whats-next-2.-guldagergaard2017.jpg" alt="52.whats next 2. guldagergaard2017"></a>
  <a href="#" onclick="openLightbox(1); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/whats-next-guldagergaard/buddhaegg2.10.53.13.jpg" alt="buddhaegg2.10.53.13"></a>
  <a href="#" onclick="openLightbox(2); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/whats-next-guldagergaard/dsc02350.jpg" alt="dsc02350"></a>
  <a href="#" onclick="openLightbox(3); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/whats-next-guldagergaard/dsc02352.jpg" alt="dsc02352"></a>
  <a href="#" onclick="openLightbox(4); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/whats-next-guldagergaard/dsc02353.jpg" alt="dsc02353"></a>
  <a href="#" onclick="openLightbox(5); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/whats-next-guldagergaard/eggroll.jpg" alt="eggroll"></a>
  <a href="#" onclick="openLightbox(6); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/whats-next-guldagergaard/rollingegg.jpg" alt="rollingegg"></a>
  <a href="#" onclick="openLightbox(7); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/whats-next-guldagergaard/upside-down10.51.08.jpg" alt="upside down10.51.08"></a>
  <a href="#" onclick="openLightbox(8); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/whats-next-guldagergaard/uups1-1.jpg" alt="uups1 1"></a>
  <a href="#" onclick="openLightbox(9); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/whats-next-guldagergaard/what-happens-next-2-1-kopio.jpg" alt="what happens next 2 1 kopio"></a>
  <a href="#" onclick="openLightbox(10); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/whats-next-guldagergaard/what-happens-next1-kopio.jpg" alt="what happens next1 kopio"></a>
  <a href="#" onclick="openLightbox(11); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/whats-next-guldagergaard/whats-next-30.9.17-11.52.53.jpg" alt="whats next 30.9.17 11.52.53"></a>
  <a href="#" onclick="openLightbox(12); return false;"><img style="object-position: 50% 50%;" src="/assets/images/art/whats-next-guldagergaard/whats-next-at-pot-viapori.jpg" alt="whats next at pot viapori"></a>
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
    "/assets/images/art/whats-next-guldagergaard/52.whats-next-2.-guldagergaard2017.jpg",
    "/assets/images/art/whats-next-guldagergaard/buddhaegg2.10.53.13.jpg",
    "/assets/images/art/whats-next-guldagergaard/dsc02350.jpg",
    "/assets/images/art/whats-next-guldagergaard/dsc02352.jpg",
    "/assets/images/art/whats-next-guldagergaard/dsc02353.jpg",
    "/assets/images/art/whats-next-guldagergaard/eggroll.jpg",
    "/assets/images/art/whats-next-guldagergaard/rollingegg.jpg",
    "/assets/images/art/whats-next-guldagergaard/upside-down10.51.08.jpg",
    "/assets/images/art/whats-next-guldagergaard/uups1-1.jpg",
    "/assets/images/art/whats-next-guldagergaard/what-happens-next-2-1-kopio.jpg",
    "/assets/images/art/whats-next-guldagergaard/what-happens-next1-kopio.jpg",
    "/assets/images/art/whats-next-guldagergaard/whats-next-30.9.17-11.52.53.jpg",
    "/assets/images/art/whats-next-guldagergaard/whats-next-at-pot-viapori.jpg"
  ];
  const galleryTitles = [
    "52.whats next 2. guldagergaard2017",
    "buddhaegg2.10.53.13",
    "dsc02350",
    "dsc02352",
    "dsc02353",
    "eggroll",
    "rollingegg",
    "upside down10.51.08",
    "uups1 1",
    "what happens next 2 1 kopio",
    "what happens next1 kopio",
    "whats next 30.9.17 11.52.53",
    "whats next at pot viapori"
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
