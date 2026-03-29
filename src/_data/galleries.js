const fs = require("fs");
const path = require("path");

function getImages(folder) {
  const dir = path.join(__dirname, "../assets/images", folder);
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir)
    .filter(f => /\.(jpg|jpeg|png|JPG|JPEG|PNG)$/i.test(f) && f !== "cover.jpg")
    .map(f => ({
      src: `/assets/images/${folder}/${f}`,
      title: f.replace(/\.[^.]+$/, "").replace(/[-_]/g, " ")
    }));
}

function getSeries(category) {
  const dir = path.join(__dirname, "../assets/images", category);
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir)
    .filter(f => fs.statSync(path.join(dir, f)).isDirectory())
    .map(series => ({
      slug: series,
      cover: `/assets/images/${category}/${series}/cover.jpg`,
      images: getImages(`${category}/${series}`)
    }));
}

module.exports = {
  uniqueCeramics: getImages("unique-ceramics"),
  tablewareCeramics: getImages("tableware-ceramics"),
  art: getImages("art"),
  tablewareSeries: getSeries("tableware-ceramics"),
  uniqueSeries: getSeries("unique-ceramics"),
  artSeries: getSeries("art")
};
