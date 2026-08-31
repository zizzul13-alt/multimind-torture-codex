(() => {
  const key = "multimind-benchmark-scroll";
  const region = () => document.querySelector("[data-scroll-region='conversation']");
  const snapshot = () => {
    const element = region();
    if (element) sessionStorage.setItem(key, String(element.scrollTop));
  };
  document.addEventListener("click", (event) => {
    if (event.target.closest("[data-morph-switch]")) snapshot();
  });
  const restore = () => {
    const value = sessionStorage.getItem(key);
    const element = region();
    if (value && element) element.scrollTop = Number(value);
  };
  new MutationObserver(() => requestAnimationFrame(restore)).observe(document.documentElement, { childList: true, subtree: true });
  window.addEventListener("load", restore);
})();
