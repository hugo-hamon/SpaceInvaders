(function () {

    document.addEventListener('DOMContentLoaded', function (event) {

        let list = document.querySelectorAll('.make-snippet');

        [].forEach.call(list, function (el) {
            let snippet = el.innerHTML.replace(/</g, '&lt;');
            snippet = snippet.replace(/ /g, '&nbsp;');
            let code = '<pre class="language-markup"><code>' + snippet + '</pre></code>';
            el.insertAdjacentHTML('afterend', code);
        });

        if (window.Prism) {
            Prism.highlightAll(false);
        }
    });

})();