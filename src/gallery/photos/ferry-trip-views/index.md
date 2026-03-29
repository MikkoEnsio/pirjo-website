---
title: Ferry Trip Views
layout: base.njk
---
# Ferry Trip Views

<div class="gallery-grid">
  <a href="#" onclick="openLightbox(0); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/ferry-trip-views/april_fog.jpg" alt="april fog"></a>
  <a href="#" onclick="openLightbox(1); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/ferry-trip-views/bubbles.jpg" alt="bubbles"></a>
  <a href="#" onclick="openLightbox(2); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/ferry-trip-views/clouds.jpg" alt="clouds"></a>
  <a href="#" onclick="openLightbox(3); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/ferry-trip-views/ferry_trip_1.jpg" alt="ferry trip 1"></a>
  <a href="#" onclick="openLightbox(4); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/ferry-trip-views/morning.JPG" alt="morning"></a>
  <a href="#" onclick="openLightbox(5); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/ferry-trip-views/november_sky.jpg" alt="november sky"></a>
  <a href="#" onclick="openLightbox(6); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/ferry-trip-views/resting.jpg" alt="resting"></a>
  <a href="#" onclick="openLightbox(7); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/ferry-trip-views/spring_arrives_early.jpg" alt="spring arrives early"></a>
  <a href="#" onclick="openLightbox(8); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/ferry-trip-views/spring_fog.jpg" alt="spring fog"></a>
  <a href="#" onclick="openLightbox(9); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/ferry-trip-views/spring_ice.jpg" alt="spring ice"></a>
  <a href="#" onclick="openLightbox(10); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/ferry-trip-views/spring_will_arrive.JPG" alt="spring will arrive"></a>
  <a href="#" onclick="openLightbox(11); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/ferry-trip-views/sunset.jpg" alt="sunset"></a>
  <a href="#" onclick="openLightbox(12); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/ferry-trip-views/thin_ice_cover.jpg" alt="thin ice cover"></a>
  <a href="#" onclick="openLightbox(13); return false;"><img style="object-position: 50% 50%;" src="/assets/images/photos/ferry-trip-views/yellow_sky.jpg" alt="yellow sky"></a>
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
  const ferryTripViewsImages = [
    "/assets/images/photos/ferry-trip-views/april_fog.jpg",
    "/assets/images/photos/ferry-trip-views/bubbles.jpg",
    "/assets/images/photos/ferry-trip-views/clouds.jpg",
    "/assets/images/photos/ferry-trip-views/ferry_trip_1.jpg",
    "/assets/images/photos/ferry-trip-views/morning.JPG",
    "/assets/images/photos/ferry-trip-views/november_sky.jpg",
    "/assets/images/photos/ferry-trip-views/resting.jpg",
    "/assets/images/photos/ferry-trip-views/spring_arrives_early.jpg",
    "/assets/images/photos/ferry-trip-views/spring_fog.jpg",
    "/assets/images/photos/ferry-trip-views/spring_ice.jpg",
    "/assets/images/photos/ferry-trip-views/spring_will_arrive.JPG",
    "/assets/images/photos/ferry-trip-views/sunset.jpg",
    "/assets/images/photos/ferry-trip-views/thin_ice_cover.jpg",
    "/assets/images/photos/ferry-trip-views/yellow_sky.jpg"
  ];

  const ferryTripViewsTitles = [
    "april fog",
    "bubbles",
    "clouds",
    "ferry trip 1",
    "morning",
    "november sky",
    "resting",
    "spring arrives early",
    "spring fog",
    "spring ice",
    "spring will arrive",
    "sunset",
    "thin ice cover",
    "yellow sky"
  ];

  let currentImageIndex = 0;

  function updateLightbox() {
    const lightboxImage = document.getElementById("lightbox-image");
    const lightboxCaption = document.getElementById("lightbox-caption");
    lightboxImage.src = ferryTripViewsImages[currentImageIndex];
    lightboxImage.alt = ferryTripViewsTitles[currentImageIndex];
    lightboxCaption.textContent = ferryTripViewsTitles[currentImageIndex];
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
    currentImageIndex = (currentImageIndex - 1 + ferryTripViewsImages.length) % ferryTripViewsImages.length;
    updateLightbox();
  }

  function nextImage(event) {
    event.stopPropagation();
    currentImageIndex = (currentImageIndex + 1) % ferryTripViewsImages.length;
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
      currentImageIndex = (currentImageIndex - 1 + ferryTripViewsImages.length) % ferryTripViewsImages.length;
      updateLightbox();
    }
    if (event.key === "ArrowRight") {
      currentImageIndex = (currentImageIndex + 1) % ferryTripViewsImages.length;
      updateLightbox();
    }
  });
</script>
