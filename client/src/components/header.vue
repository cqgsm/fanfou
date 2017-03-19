<template>
    <header class="header border-1px">
        <slot name="left">
            <div class="item left"></div>
        </slot>
        <h2 class="title">{{title}}</h2>
        <slot name="right">
            <div class="item right"></div>
        </slot>
    </header>
</template>
<script>
    export default {
        props: {
            title: {
                type: String,
                default: '乐寻'
            }
        }
    }
</script>
<style lang="scss"> 
    @import '../../static/scss/base.scss';
    .header{
        background: #f34d41;
        display: flex;
        font-size: 14px;
        color: #fff;
        justify-content: space-between;
        align-items: center;
        padding: 0 20px;
        position: absolute;
        right: 0;
        left: 0;
        top: 0;
        z-index: 1000;
        height: 50px;
        line-height: 50px;
        @include border-1px(#ddd);
        .item{
            width: 50px;
        }
        .left{
            text-align: left;
        }
        .right{
            text-align: right;
        }
        .title{
            overflow: hidden;
            padding: 0;
            margin: 0;
            text-align: center;
            font-size: 16px;
            white-space: nowrap;
            text-overflow: ellipsis;
        }
    }
</style>