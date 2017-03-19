<template>
    <transition name="fade">
        <span v-show="show" class="toast">
            {{toasttext}}
        </span>
    </transition>
</template>
<script>
    export default {
        data () {
            return {
                show: false
            }
        },
        props: {
            time: {
                type: Number,
                default: 2000
            },
            // 是否显示
            toastshow: {
                type: Boolean,
                required: false,
                default: function () {
                    return false;
                }
            },
            // 提示内容
            toasttext: {
                type: String,
                required: false,
                default: function () {
                    return '不能为空'
                }
            }
        },
        watch: {
            toastshow: function (newValue, oldValue) {
                if (newValue) {
                    clearTimeout(this.timeout);
                    this.show = true;
                    this.timeout = setTimeout(() => {
                        this.show = false;
                    }, this.time);
                }
            }
        }
    }
</script>
<style lang="scss" scoped>
    .toast{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        max-width: 80%;
        border-radius: 5px;
        background: rgba(0, 0, 0, 0.7);
        color: #fff;
        box-sizing: border-box;
        z-index: 10000;
        padding: 10px;
        transition: opacity .2s linear;
    }
    .fade-enter, .fade-leave-active {
        opacity: 0
    }
</style>