jQuery(document).ready(function() {
    var galleryTop = new Swiper('.pc_ban', {
        on: {
            init: function() {
                swiperAnimateCache(this);
                swiperAnimate(this);
            },
            slideChangeTransitionEnd: function() {
                swiperAnimate(this);
            }
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        centeredSlides: true,
        paginationClickable: true,
        slideToClickedSlide: true,
        autoplayDisableOnInteraction: false,
        autoplay: {
            delay: 5000,
            disableOnInteraction: false,
        },
        speed: 1000,
        loop: true,
    });
    var galleryThumbs = new Swiper('.test_ban', {
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },

        spaceBetween: 20,
        paginationClickable: true,
        slideToClickedSlide: true,
        autoplay: {
            delay: 5000,
            disableOnInteraction: false,
        },
        loop: true,

    });
    var galleryThumbs = new Swiper('.pr_ban', {
        navigation: {
            nextEl: '.swiper-button-next-pr',
            prevEl: '.swiper-button-prev-pr',
        },
        spaceBetween: 20,
        paginationClickable: true,
        slideToClickedSlide: true,
        autoplay: {
            delay: 5000,
            disableOnInteraction: false,
        },
        loop: true,
        breakpoints: {
            992: {
                slidesPerView: 4,
                spaceBetween: 10,
            },
            0: {
                slidesPerView: 2,
                spaceBetween: 10,
            },
        },
    });
    var galleryThumbs = new Swiper('.sq1', {
        navigation: {
            nextEl: '.swiper-button-next_sq1',
            prevEl: '.swiper-button-prev_sq1',
        },
        pagination: {
            el: '.swiper-pagination_sq1',
            clickable: true,
        },
        centeredSlides: true,
        paginationClickable: true,
        slideToClickedSlide: true,
        autoplayDisableOnInteraction: false,
        autoplay: {
            delay: 5000,
            disableOnInteraction: false,
        },
        loop: true,
        speed: 1000,
        breakpoints: {
            992: {
                slidesPerView: 3,
                spaceBetween: 20,
            },
            640: {
                slidesPerView: 1,
                spaceBetween: 10,
            },
        },
    });


    jQuery(window).scroll(function() {
        var top = jQuery(window).scrollTop();
        var hd = jQuery(".header").height();
        if (top > hd) {
            jQuery(".header").addClass("on");
            jQuery(".header .container").addClass("on");
            jQuery(".nav div").addClass("on");
            jQuery(".header .logo .yd_on").addClass("on");
            jQuery(".header .logo  .yd_on1").addClass("on1");
        } else {
            jQuery(".header").removeClass("on");
            jQuery(".header .container").removeClass("on");
            jQuery(".nav div").removeClass("on");
            jQuery(".header .logo .yd_on").removeClass("on");
            jQuery(".header .logo .yd_on1").removeClass("on1");
        }
    });



    jQuery(".header .an").click(function() {
        jQuery("html").addClass("on");
        jQuery("body").addClass("on");
        jQuery(".sj_bj").slideDown(0);
        jQuery(".nav").find(".e_j").slideUp();
        jQuery(this).addClass("n");
    });
    jQuery(".sj_bj").click(function() {
        jQuery(".header .an").removeClass("n");
        jQuery(".sj_bj").slideUp(0);
        jQuery("html").removeClass("on");
        jQuery("body").removeClass("on");
        jQuery(".nav").find(".e_j").slideUp();
    });
    jQuery(".nav .y_j i").click(function() {
        jQuery(this).parent(".y_j").siblings(".e_j").slideToggle();
        jQuery(this).parents("li").siblings().find(".e_j").slideUp();
    });
    jQuery('.header .icon-search').click(function() {
        jQuery(".search_none").filter(':not(:animated)').slideDown();
    });
    jQuery('.sc_gb').click(function() {
        jQuery(".search_none").slideUp();

    });



    jQuery(".w_x").click(function() {
        jQuery(".e_m").slideDown();
    });
    jQuery(".e_m").click(function() {
        jQuery(this).slideUp();
    });


// 视频




});