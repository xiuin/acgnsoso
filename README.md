

## 信息
- acgnsoso使用主题：koji

## 改动
#### 菜单栏自定义：
  - 汉服（category）
  - JK制服（category）
  - 洛丽塔lo裙（category）
  - 优惠券（url：https://acgnsoso.com/wp-content/apps/coupon/hanfu.htm）

#### css改动
```
# 改动padding（改成：padding: 5rem 4rem 0 4rem;）

#site-header {
    background: none;
    display: flex;
    flex-direction: column;
    justify-content: stretch;
    padding: 8rem 4rem 0 4rem;
}
#site-header {
	padding: 12rem 8rem 0 8rem;
}
```

#### footer改动
```
<p class="credits">
	<?php
	/* Translators: $s = name of the theme developer */
	/* printf( _x( 'Theme by %s', 'Translators: $s = name of the theme developer', 'koji' ), '<a href="https://www.andersnoren.se">' . __( 'Anders Norén', 'koji' ) . '</a>' ); ?> */

	printf( esc_html__( '©Copyright 2020', 'scratchpad' ) ); ?>
	<span class="sep"> | </span>
	<?php printf( esc_html__( 'Cherry Pie', 'scratchpad' ) ); ?>
	<span class="sep"> | </span>
	<?php printf( esc_html__( 'contact@mail.cherrysoso.com', 'scratchpad' ) ); ?>
</p><!-- .credits -->
```

---

## 准备
- 在淘宝联盟把表格导出，另存为csv，放到alimama文件夹

## 运行
```
cd source
python3 run.py
```
生成结果在coupon文件夹

## 发布
```
./deploy.sh
```