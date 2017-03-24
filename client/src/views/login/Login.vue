<template>
    <div class="loginContainer">
        <!--<v-header>
            <div slot="left" class="item left">
                后退
            </div>
            <div slot="right" class="item right">
                前进
            </div>
        </v-header>-->
        <mt-header title="标题过长会隐藏后面的内容啊哈哈哈哈">
            <router-link to="/" slot="left">
                <mt-button icon="back">返回</mt-button>
            </router-link>
            <mt-button icon="more" slot="right"></mt-button>
        </mt-header>

        <div class="main">
            <form @submit.prevent="submit">
                <div class="input-field">
                    <label>账号</label>
                    <input type="tel" placeholder="请输入手机号码" v-model.number="user_phone">
                    <span></span>
                </div>
                <div class="input-field">
                    <label>密码</label>
                    <input type="text" placeholder="请输入密码" v-model="user_password">
                    <span></span>
                </div>
                <button class="btn">
                    {{btn_status ? '正在登陆中':'登陆'}}
                </button>
            </form>
            <a href="#" class="forget">登陆遇到问题？</a>
        </div>



        <div class="footer">
            <span>微信登陆</span>
        </div>

    </div>
</template>
<script>
    export default {
        name: 'login',
        data() {
            return {
                user_phone: '',
                user_password: '',
                btn_status: false // true正在提交， false还没提交
            }
        }
    }
</script>
<style lang="scss">
@import '../../../static/scss/base.scss';
    .loginContainer{
        .main{
            padding: 0 20px;
            .input-field,
            .input-field *{
                -webkit-box-sizing: border-box;
                box-sizing:border-box;
            }
            .input-field {
                position: relative;
                font-size: 16px;
                color: #000;
                display: flex;
                height: 50px;
                line-height: 50px;
                label{
                    flex: 0 0 50px;
                }
                & > input{
                    background-color: transparent;
                    border: none;
                    border-radius: 0;
                    height:50px;
                    line-height: 50px;
                    width: 100%;
                    padding: 0;
                    box-shadow: none;
                    outline: none;
                    -webkit-transition: all 0.3s;
                    transition: all 0.3s;
                }
                & > input+span{
                    position: absolute;
                    top: 100%;
                    left: 0;
                    display: inline-block;
                    max-width: 100%;
                    z-index: 0;
                    width: 100%;
                    height: 2px;
                    border-bottom: 1px solid #d9d9d9;
                }
                span:after{
                    content: "";
                    position: absolute;
                    bottom: 0;
                    left: 0;
                    width: 100%;
                    height: 1px;
                    background: #df2d2d;
                    -webkit-transform: scale(0);
                    transform: scale(0);
                    -webkit-transition: all .2s ease-out;
                    transition: all .2s ease-out;
                }
                input:focus+span:after {
                    -webkit-transform: scale(1);
                    transform: scale(1);
                }
            }
            .btn{
                width: 100%;
                height: 42px;
                background: #d76c6c;
                border-radius: 5px;
                margin-top: 20px;
                font-size: 16px;
                color: #fff;
                text-align: center;
                line-height: 42px;
            }
            .forget{
                display: block;
                text-align: center;
                margin-top: 10px;
                font-size: 12px;
            }
        }
        .footer{
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translate(-50%, 0);
            &>span{
                color: green;
                text-shadow:0 1px hsl(0,0%,85%),
                            0 2px hsl(0,0%,80%),
                            0 3px hsl(0,0%,75%),0 4px hsl(0,0%,70%),
                            0 5px hsl(0,0%,65%),
                            0 5px 10px black;
               font-size: 18px;             
            }
        }
    }
</style>