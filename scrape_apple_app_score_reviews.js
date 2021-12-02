let store = require("app-store-scraper");
let fs = require("fs");

// These apps were selected because they had the highest discrepancy between ratings on the Google Play Store compared to Apple App Store
let app_ids = [
  "com.fanduel.scout",
  "co.mixcord.acapella",
  "com.kinetic.fit",
  "com.geniecompany.OHDAnywhere",
  "com.pollardbanknote.PlayOnKS",
  "com.ombiel.campusm.mdc",
  "com.proxypics.app",
  "com.lipsar.cannondemolition",
  "subway.schoox",
  "com.prime.on",
];

let extract_on_page_reviews = (reviews, app_id) => {
  for (const review of reviews) {
    let user_name = review["userName"];
    let score = review["score"];
    let content = review["text"];

    // From https://stackoverflow.com/questions/10805125/how-to-remove-all-line-breaks-from-a-string
    user_name = user_name.replace(/(\r\n|\n|\r|;)/gm, "");
    content = content.replace(/(\r\n|\n|\r|;)/gm, "");

    entry =
      String(app_id) +
      ";" +
      String(user_name) +
      ";" +
      String(score) +
      ";" +
      String(content) +
      "\n";

    fs.appendFile("apple_app_reviews.csv", entry, (error) => {
      if (error) throw error;
    });
  }
};

let extract_reviews = (app_id) => {
  let pages = [1, 2]; // 50 reviews per page
  pages.forEach((page) => {
    store
      .reviews({
        appId: app_id,
        sort: store.sort.HELPFUL,
        page: page,
      })
      .then((reviews) => {
        extract_on_page_reviews(reviews, app_id);
      })
      .catch((error) => {
        console.log(error);
      });
  });
};

// Get the reviews for each app
for (let app_id of app_ids) {
  extract_reviews(app_id);
}
