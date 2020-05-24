
tpl_content = '''
<article class="preview preview-post do-spot post-52 post type-post status-publish format-standard has-post-thumbnail hentry category-jk has-thumbnail will-be-spotted spotted" id="post-52" style="position: absolute; left: 33.2504%; top: 0px;">
	<div class="preview-wrapper">
		<a  class="preview-image">
			<img width="602" height="602" src="{img_url}" class="attachment-koji_preview_image_high_resolution size-koji_preview_image_high_resolution wp-post-image" alt="" sizes="(max-width: 602px) 100vw, 602px">
		</a>
		<div class="preview-inner">
			<h4 class="preview-title" style="font-size:12px;">{title}</h4>
			<h5 class="preview-title" style="font-size:12px;color:#bbbbbb;">用券后 <span style="color:#f9b698;">¥{final_price}</span>&nbsp;&nbsp;&nbsp;现价¥{current_price}</h5>
			<button class="coupon-btn" onclick="window.open('{coupon_url}');">
				<span>¥</span>
				<span class="coupon-amount">{coupon_price}</span>
				<span class="btn-name">立即领券</span>
				<p class="coupon-date">使用期限 {coupon_date}</p>
			</button>
		</div><!-- .preview-inner -->
	</div><!-- .preview-wrapper -->
</article>
'''

tpl_page = '''
<!DOCTYPE html>
<html class="no-js" lang="zh-CN">
<head>
<meta http-equiv="content-type" content="text/html" charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" >
<link rel="profile" href="http://gmpg.org/xfn/11">

	<!-- This site is optimized with the Yoast SEO plugin v14.1 - https://yoast.com/wordpress/plugins/seo/ -->
	<title>{title} - 二次元三坑小站</title>
	<meta name="description" content="二次元三坑小站" />
	<meta name="robots" content="index, follow" />
	<meta name="googlebot" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
	<meta name="bingbot" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
	<link rel="canonical" href="https://acgnsoso.com/" />
	<meta property="og:locale" content="zh_CN" />
	<meta property="og:type" content="website" />
	<meta property="og:title" content="{title} - 二次元三坑小站" />
	<meta property="og:description" content="二次元三坑小站" />
	<meta property="og:url" content="https://acgnsoso.com/" />
	<meta property="og:site_name" content="ACGN-SOSO" />
	<meta name="twitter:card" content="summary_large_image" />
	
	<!-- / Yoast SEO plugin. -->


<link rel='dns-prefetch' href='//s.w.org' />
<link rel='stylesheet' id='wp-block-library-css'  href='https://acgnsoso.com/wp-includes/css/dist/block-library/style.min.css?ver=5.4.1' type='text/css' media='all' />
<link rel='stylesheet' id='wp-pagenavi-css'  href='https://acgnsoso.com/wp-content/plugins/wp-pagenavi/pagenavi-css.css?ver=2.70' type='text/css' media='all' />
<link rel='stylesheet' id='koji-style-css'  href='https://acgnsoso.com/wp-content/themes/koji/style.css?ver=2.0.5' type='text/css' media='all' />
<script type='text/javascript' src='https://acgnsoso.com/wp-includes/js/jquery/jquery.js?ver=1.12.4-wp'></script>
<script type='text/javascript' src='https://acgnsoso.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=1.4.1'></script>
<link rel='https://api.w.org/' href='https://acgnsoso.com/wp-json/' />
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://acgnsoso.com/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://acgnsoso.com/wp-includes/wlwmanifest.xml" /> 
<meta name="generator" content="WordPress 5.4.1" />
<script>document.documentElement.className = document.documentElement.className.replace( 'no-js', 'js' );</script>
<link rel="icon" href="https://acgnsoso.com/wp-content/uploads/sites/3/2020/05/柠檬黑-150x150.png" sizes="32x32" />
<link rel="icon" href="https://acgnsoso.com/wp-content/uploads/sites/3/2020/05/柠檬黑-200x200.png" sizes="192x192" />
<link rel="apple-touch-icon" href="https://acgnsoso.com/wp-content/uploads/sites/3/2020/05/柠檬黑-200x200.png" />
<meta name="msapplication-TileImage" content="https://acgnsoso.com/wp-content/uploads/sites/3/2020/05/柠檬黑.png" />

<style>
.coupon-date {{
	font-size:8px;
	color:rgba(255, 255, 255, 0.67);
}}
.btn-name {{
	padding-left: 6px;
}}
.coupon-amount {{
	font-size:30px;
}}
.coupon-btn {{
	padding: 5px;
	width: 100%;
	background: url(https://gw.alicdn.com/tfs/TB16d.1ykPoK1RjSZKbXXX1IXXa-665-115.png_720x720.jpg_.webp); background-size: 100% 100%;
}}
</style>

	</head>

	<body class="home blog logged-in pagination-type-button">
		<div id="site-wrapper">
			<header id="site-header" role="banner">
				<a class="skip-link" href="#site-content">Skip to the content</a>
				<a class="skip-link" href="#main-menu">Skip to the main menu</a>
				<div class="header-top section-inner">
						<h1 class="site-title"><a href="https://acgnsoso.com/">{title}</a></h1>
					<button type="button" aria-pressed="false" class="toggle nav-toggle" data-toggle-target=".mobile-menu-wrapper" data-toggle-scroll-lock="true" data-toggle-attribute="">
						<label>
							<span class="show">Menu</span>
							<span class="hide">Close</span>
						</label>
						<div class="bars">
							<div class="bar"></div>
							<div class="bar"></div>
							<div class="bar"></div>
						</div><!-- .bars -->
					</button><!-- .nav-toggle -->
				</div><!-- .header-top -->

				<div class="header-inner section-inner">
					<div class="header-inner-top">
							<p class="site-description">二次元三坑小站</p>
						<ul class="site-nav reset-list-style" id="main-menu" role="navigation">
							<li id="menu-item-39" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-39"><a href="https://acgnsoso.com/category/hanfu/">汉服</a></li>
<li id="menu-item-43" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-43"><a href="https://acgnsoso.com/category/jk/">JK制服</a></li>
<li id="menu-item-44" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-44"><a href="https://acgnsoso.com/category/lolita/">洛丽塔lo裙</a></li>
<li id="menu-item-49" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-49"><a href="https://acgnsoso.com/wp-content/apps/coupon/hanfu.htm" >优惠券</a>

<ul class="sub-menu">
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item--2021373315287902200"><a href="https://acgnsoso.com/wp-content/apps/coupon/hanfu.htm" class="customize-unpreviewable" style="font-size:10px;">汉服优惠券</a></li>
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item--2021373315287902200"><a href="https://acgnsoso.com/wp-content/apps/coupon/jk.htm" class="customize-unpreviewable" style="font-size:10px;">JK优惠券</a></li>
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item--2021373315287902200"><a href="https://acgnsoso.com/wp-content/apps/coupon/lolita.htm" class="customize-unpreviewable" style="font-size:10px;">洛丽塔优惠券</a></li>
</ul>

</li>
						</ul>
					</div><!-- .header-inner-top -->

					<div class="social-menu-wrapper">
							<ul class="social-menu reset-list-style social-icons s-icons">
									<li class="search-toggle-wrapper"><button type="button" aria-pressed="false" data-toggle-target=".search-overlay" data-set-focus=".search-overlay .search-field" class="toggle search-toggle"><span class="screen-reader-text">Toggle the search field</span></button></li>
							</ul><!-- .social-menu -->
					</div><!-- .social-menu-wrapper -->
				</div><!-- .header-inner -->
			</header><!-- #site-header -->

			<div class="mobile-menu-wrapper" aria-expanded="false">

				<div class="mobile-menu section-inner">

					<div class="mobile-menu-top">
							<p class="site-description">二次元三坑小站</p>
						<ul class="site-nav reset-list-style" id="mobile-menu" role="navigation">
							<li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-39"><a href="https://acgnsoso.com/category/hanfu/">汉服</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-43"><a href="https://acgnsoso.com/category/jk/">JK制服</a></li>
<li class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-44"><a href="https://acgnsoso.com/category/lolita/">洛丽塔lo裙</a></li>
<li id="menu-item-49" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-49"><a href="https://acgnsoso.com/wp-content/apps/coupon/hanfu.htm" >优惠券</a>

<ul class="sub-menu">
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item--2021373315287902200"><a href="https://acgnsoso.com/wp-content/apps/coupon/hanfu.htm" class="customize-unpreviewable" style="font-size:10px;">汉服优惠券</a></li>
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item--2021373315287902200"><a href="https://acgnsoso.com/wp-content/apps/coupon/jk.htm" class="customize-unpreviewable" style="font-size:10px;">JK优惠券</a></li>
	<li class="menu-item menu-item-type-custom menu-item-object-custom menu-item--2021373315287902200"><a href="https://acgnsoso.com/wp-content/apps/coupon/lolita.htm" class="customize-unpreviewable" style="font-size:10px;">洛丽塔优惠券</a></li>
</ul>

</li>
						</ul>


					</div><!-- .mobile-menu-top -->

					<div class="social-menu-wrapper">
							<ul class="social-menu reset-list-style social-icons s-icons mobile">
									<li class="search-toggle-wrapper"><button type="button" aria-pressed="false" data-toggle-target=".search-overlay" data-set-focus=".search-overlay .search-field" class="toggle search-toggle"><span class="screen-reader-text">Toggle the search field</span></button></li>
							</ul><!-- .social-menu -->
					</div><!-- .social-menu-wrapper -->
				</div><!-- .mobile-menu -->
			</div><!-- .mobile-menu-wrapper -->

				<div class="search-overlay cover-modal" aria-expanded="false">
					<div class="section-inner search-overlay-form-wrapper">
<form role="search" method="get" class="search-form" action="https://acgnsoso.com/">
	<label for="search-form-5eca7b462203d">
		<span class="screen-reader-text">Search for:</span>
		<img aria-hidden="true" src="https://acgnsoso.com/wp-content/themes/koji/assets/images/icons/spyglass.svg" />
	</label>
	<input type="search" id="search-form-5eca7b462203d" class="search-field" placeholder="Enter your search query" value="" name="s" />
	<button type="submit" class="search-submit screen-reader-text">Search</button>
</form>
					</div><!-- .section-inner -->

					<button type="button" class="toggle search-untoggle" data-toggle-target=".search-overlay" data-set-focus=".search-toggle:visible">
						<div class="search-untoggle-inner">
							<img aria-hidden="true" src="https://acgnsoso.com/wp-content/themes/koji/assets/images/icons/cross.svg" />
						</div>
						<span class="screen-reader-text">Hide the search overlay</span>
					</button><!-- .search-untoggle -->

				</div><!-- .search-overlay -->


<main id="site-content" role="main">
	<div class="section-inner">
		<div class="posts load-more-target" id="posts" aria-live="polite">
			<div class="grid-sizer"></div>


{content}



		</div><!-- .posts -->
	</div><!-- .section-inner -->
</main><!-- #site-content -->

<footer id="site-footer" role="contentinfo">
<p class="credits">
		©Copyright 2020					<span class="sep"> | </span>
		Cherry Pie					<span class="sep"> | </span>
		contact@mail.cherrysoso.com				</p><!-- .credits -->
</footer><!-- #site-footer -->

<script type='text/javascript' src='https://acgnsoso.com/wp-includes/js/imagesloaded.min.js?ver=3.2.0'></script>
<script type='text/javascript' src='https://acgnsoso.com/wp-includes/js/masonry.min.js?ver=3.3.2'></script>
<script type='text/javascript' src='https://acgnsoso.com/wp-content/themes/koji/assets/js/construct.js?ver=2.0.5'></script>
<script type='text/javascript' src='https://acgnsoso.com/wp-includes/js/wp-embed.min.js?ver=5.4.1'></script>

		</div><!-- #site-wrapper -->

	</body>
</html>

'''


test = '''
<style>
.coupon-date {
	font-size:8px;
	color:rgba(255, 255, 255, 0.67);
}
.btn-name {
	padding-left: 6px;
}
.coupon-amount {
	font-size:30px;
}
.coupon-btn {
	padding: 5px;
	width: 100%;
	background: url(https://gw.alicdn.com/tfs/TB16d.1ykPoK1RjSZKbXXX1IXXa-665-115.png_720x720.jpg_.webp); background-size: 100% 100%;
}
</style>

<article class="preview preview-post do-spot post-52 post type-post status-publish format-standard has-post-thumbnail hentry category-jk has-thumbnail will-be-spotted spotted" id="post-52" style="position: absolute; left: 33.2504%; top: 0px;">
	<div class="preview-wrapper">
		<a  class="preview-image">
			<img width="602" height="602" src="https://img.alicdn.com/i2/2089051013/O1CN01tP6FpI1JLzoAULrOA_!!2089051013.jpg" class="attachment-koji_preview_image_high_resolution size-koji_preview_image_high_resolution wp-post-image" alt="" sizes="(max-width: 602px) 100vw, 602px">
		</a>
		<div class="preview-inner">
			<h4 class="preview-title" style="font-size:12px;">花信集原创汉服《好运莲莲》一片式穿孔对襟6米齐胸襦裙汉服女</h4>
			<h5 class="preview-title" style="font-size:12px;color:#bbbbbb;">用券后 <span style="color:#f9b698;">¥108</span>&nbsp;&nbsp;&nbsp;现价¥128</h5>
			<button class="coupon-btn" onclick="window.open('https://uland.taobao.com/coupon/edetail?e=%2F8qHhLdmqf8NfLV8niU3R5TgU2jJNKOfNNtsjZw%2F%2FoKsz7C4vRtwTeIuJEB2tLC9a3WOxRNxrt4cOO0ZyfUC7MuRTiT9oEhVZV8pr6FWc0Pa7kmlFu9PUxTe%2FiWFV1xkmMHpNfYdHdD%2FawWiow74mICnqiGk4FiOLJ3bdz5Kbzzmt4OzLcG%2BoXaC54LfKGbLonv6QcvcARY%3D&&app_pvid=59590_11.20.221.218_525_1589652044790&ptl=floorId:31507;app_pvid:59590_11.20.221.218_525_1589652044790;tpp_pvid:&union_lens=lensId%3AOPT%401589652044%400b14ddda_e28f_1721ea53c41_3295%4001');">
				<span>¥</span>
				<span class="coupon-amount">20</span>
				<span class="btn-name">立即领券</span>
				<p class="coupon-date">使用期限 05.10-06.03</p>
			</button>
		</div><!-- .preview-inner -->
	</div><!-- .preview-wrapper -->
</article>
'''