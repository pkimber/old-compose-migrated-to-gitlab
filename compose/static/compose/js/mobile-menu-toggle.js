(function (window, document) {
var menu = document.getElementById('menu'),
    WINDOW_CHANGE_EVENT = ('onorientationchange' in window) ? 'orientationchange':'resize';

function toggleMenuClass() {
    [].forEach.call(
        document.getElementById('menu').querySelectorAll('.mobile-menu-can-transform'),
        function(el){
            var menuClass = el.getAttribute('data-menu-class');
            if (menuClass != '') {
                el.classList.toggle(menuClass);
            }
        }
    );
};

function toggleMenu() {
    // set timeout so that the panel has a chance to roll up
    // before the menu switches states
    if (menu.classList.contains('open')) {
        setTimeout(toggleMenuClass, 500);
    }
    else {
        toggleMenuClass();
    }
    menu.classList.toggle('open');
    document.getElementById('toggle').classList.toggle('x');
};

function closeMenu() {
    if (menu.classList.contains('open')) {
        toggleMenu();
    }
}

document.getElementById('toggle').addEventListener('click', function (e) {
    toggleMenu();
    e.preventDefault();
});

window.addEventListener(WINDOW_CHANGE_EVENT, closeMenu);
})(this, this.document);
