module.exports = function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy("src/assets");
  
  eleventyConfig.addCollection("blog", function(collectionApi) {
    return collectionApi.getFilteredByGlob("./src/blog/2*.md")
      .sort((a, b) => b.date - a.date);
  });
};
