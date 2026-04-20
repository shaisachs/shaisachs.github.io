function getCurrentSeason() {
  const now = new Date();
  const month = now.getMonth(); // 0 = Jan, 11 = Dec

  if (month >= 2 && month <= 4) {
    return "spring"; // March–May
  } else if (month >= 5 && month <= 7) {
    return "summer"; // June–August
  } else if (month >= 8 && month <= 10) {
    return "fall"; // September–November
  } else {
    return "winter"; // December–February
  }
}

function setSeasonalHeaderBackground() {
  const header = document.querySelector("#header");
  if (!header) return;

  const season = getCurrentSeason();
  header.style.background = `url(../img/bg-${season}.jpg) no-repeat center center scroll`;
}

setSeasonalHeaderBackground();