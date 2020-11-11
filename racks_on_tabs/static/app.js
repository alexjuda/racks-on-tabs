(function () {
    window.addEventListener('load', _evt => {
        const obs = new IntersectionObserver(entries => {
            console.log(entries);
            document.querySelector('#debug-p').textContent = (entries[0].isIntersecting ? "intersecting": "not intersecting");
        }, {});
        obs.observe(document.querySelector('#post-table-p'))
    });
})();
