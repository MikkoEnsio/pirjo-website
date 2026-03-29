---
title: Tulips
layout: base.njk
---
# Tulips

<div class="gallery-grid">
  <a href="#" onclick="openLightbox(0); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/big_bunch.jpg" alt="big bunch"></a>
  <a href="#" onclick="openLightbox(1); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/bud.jpg" alt="bud"></a>
  <a href="#" onclick="openLightbox(2); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/day_is_done.jpg" alt="day is done"></a>
  <a href="#" onclick="openLightbox(3); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/drop_out.jpg" alt="drop out"></a>
  <a href="#" onclick="openLightbox(4); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/fallen.jpg" alt="fallen"></a>
  <a href="#" onclick="openLightbox(5); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/fallen_loaner.jpg" alt="fallen loaner"></a>
  <a href="#" onclick="openLightbox(6); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/goodby.jpg" alt="goodby"></a>
  <a href="#" onclick="openLightbox(7); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/it_is_done.jpg" alt="it is done"></a>
  <a href="#" onclick="openLightbox(8); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/lilac_light.jpg" alt="lilac light"></a>
  <a href="#" onclick="openLightbox(9); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/lilac_tulips.jpg" alt="lilac tulips"></a>
  <a href="#" onclick="openLightbox(10); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/mysterious.jpg" alt="mysterious"></a>
  <a href="#" onclick="openLightbox(11); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/orange_tulips.jpg" alt="orange tulips"></a>
  <a href="#" onclick="openLightbox(12); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/pink.jpg" alt="pink"></a>
  <a href="#" onclick="openLightbox(13); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/pink_and_white.jpg" alt="pink and white"></a>
  <a href="#" onclick="openLightbox(14); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/pink_celebration.jpg" alt="pink celebration"></a>
  <a href="#" onclick="openLightbox(15); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/spring.jpeg" alt="spring"></a>
  <a href="#" onclick="openLightbox(16); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/tulip_buds.jpg" alt="tulip buds"></a>
  <a href="#" onclick="openLightbox(17); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/tulip_cloud.jpg" alt="tulip cloud"></a>
  <a href="#" onclick="openLightbox(18); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/tulip_stamens.jpg" alt="tulip stamens"></a>
  <a href="#" onclick="openLightbox(19); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/tulips_gone.jpg" alt="tulips gone"></a>
  <a href="#" onclick="openLightbox(20); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/white.jpg" alt="white"></a>
  <a href="#" onclick="openLightbox(21); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/tulips/white_beauty.jpg" alt="white beauty"></a>
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
  const tulipsImages = [
    "/assets/images/photos/tulips/big_bunch.jpg",
    "/assets/images/photos/tulips/bud.jpg",
    "/assets/images/photos/tulips/day_is_done.jpg",
    "/assets/images/photos/tulips/drop_out.jpg",
    "/assets/images/photos/tulips/fallen.jpg",
    "/assets/images/photos/tulips/fallen_loaner.jpg",
    "/assets/images/photos/tulips/goodby.jpg",
    "/assets/images/photos/tulips/it_is_done.jpg",
    "/assets/images/photos/tulips/lilac_light.jpg",
    "/assets/images/photos/tulips/lilac_tulips.jpg",
    "/assets/images/photos/tulips/mysterious.jpg",
    "/assets/images/photos/tulips/orange_tulips.jpg",
    "/assets/images/photos/tulips/pink.jpg",
    "/assets/images/photos/tulips/pink_and_white.jpg",
    "/assets/images/photos/tulips/pink_celebration.jpg",
    "/assets/images/photos/tulips/spring.jpeg",
    "/assets/images/photos/tulips/tulip_buds.jpg",
    "/assets/images/photos/tulips/tulip_cloud.jpg",
    "/assets/images/photos/tulips/tulip_stamens.jpg",
    "/assets/images/photos/tulips/tulips_gone.jpg",
    "/assets/images/photos/tulips/white.jpg",
    "/assets/images/photos/tulips/white_beauty.jpg"
  ];

  const tulipsTitles = [
    "big bunch",
    "bud",
    "day is done",
    "drop out",
    "fallen",
    "fallen loaner",
    "goodby",
    "it is done",
    "lilac light",
    "lilac tulips",
    "mysterious",
    "orange tulips",
    "pink",
    "pink and white",
    "pink celebration",
    "spring",
    "tulip buds",
    "tulip cloud",
    "tulip stamens",
    "tulips gone",
    "white",
    "white beauty"
  ];

  let currentImageIndex = 0;

  function updateLightbox() {
    const lightboxImage = document.getElementById("lightbox-image");
    const lightboxCaption = document.getElementById("lightbox-caption");
    lightboxImage.src = tulipsImages[currentImageIndex];
    lightboxImage.alt = tulipsTitles[currentImageIndex];
    lightboxCaption.textContent = tulipsTitles[currentImageIndex];
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
    currentImageIndex = (currentImageIndex - 1 + tulipsImages.length) % tulipsImages.length;
    updateLightbox();
  }

  function nextImage(event) {
    event.stopPropagation();
    currentImageIndex = (currentImageIndex + 1) % tulipsImages.length;
    updateLightbox();
  }

  function lightboxBackgroundClick(event) {
    if (event.target.id === "lightbox") {
      closeLightbox();
    }
  }

  document.addEventListener("keydown", function(event) {
    const lightbox = document.getElementById("lightbox");
    if (lightbox.style.display !== "flex") return;

    if (event.key === "Escape") closeLightbox();
    if (event.key === "ArrowLeft") {
      currentImageIndex = (currentImageIndex - 1 + tulipsImages.length) % tulipsImages.length;
      updateLightbox();
    }
    if (event.key === "ArrowRight") {
      currentImageIndex = (currentImageIndex + 1) % tulipsImages.length;
      updateLightbox();
    }
  });
</script>
