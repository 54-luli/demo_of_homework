
jinshanyun = "金山云"

computing_resource = (
                    """
                        <style>
                            a {
                                text-decoration:none;
                            }
                        </style>
                    """,
                    """
                    #### ● [云服务器(KEC)](https://docs.ksyun.com/products/24)\n
                    #### ● [GPU云服务器](https://docs.ksyun.com/products/1)\n
                    #### ● [云函数](https://docs.ksyun.com/products/220)\n
                    #### ● [容器服务(KCE)](https://docs.ksyun.com/products/46)
                    """
)

big_data = (
                    """
                        <style>
                            a {
                                text-decoration:none;
                            }
                        </style>
                    """,
                    """
                    #### ● [托管Hadoop(KMR)](https://docs.ksyun.com/products/35/)\n
                    #### ● [数据仓库(KDW)](https://docs.ksyun.com/products/78)\n
                    #### ● [大数据云平台](https://docs.ksyun.com/products/65)
                    """
)

database = (
                    """
                        <style>
                            a {
                                text-decoration:none;
                            }
                        </style>
                    """,
                    """
                    #### ● [关系型数据库(KRDS)](https://docs.ksyun.com/products/7)\n
                    #### ● [云数据库Redis(KCS)](https://docs.ksyun.com/products/28)\n
                    #### ● [云数据库MongoDB](https://docs.ksyun.com/products/22)
                    """
)

network = (
                    """
                        <style>
                            a {
                                text-decoration:none;
                            }
                        </style>
                    """,
                    """
                    #### ● [经典型负载均衡(SLB)](https://docs.ksyun.com/products/32)\n
                    #### ● [虚拟私有网络(VPC)](https://docs.ksyun.com/products/3)\n
                    #### ● [弹性IP(EIP)](https://docs.ksyun.com/products/23)
                    """
)

storage_cloud_distribution = (
                    """
                        <style>
                            a {
                                text-decoration:none;
                            }
                        </style>
                    """,
                    """
                    #### ● [CDN](https://docs.ksyun.com/products/5)\n
                    #### ● [对象存储(KS3)](https://docs.ksyun.com/products/25)\n
                    #### ● [云硬盘(EBS)](https://docs.ksyun.com/products/29)
                    """
)

video_cloud_services = (
                    """
                        <style>
                            a {
                                text-decoration:none;
                            }
                        </style>
                    """,
                    """
                    #### ● [云直播(KLS)](https://docs.ksyun.com/products/30)\n
                    #### ● [云转码(KET)](https://docs.ksyun.com/products/34)\n
                    #### ● [金山云魔镜](https://docs.ksyun.com/products/113)
                    """
)

cloud_security = (
                    """
                        <style>
                            a {
                                text-decoration:none;
                            }
                        </style>
                    """,
                    """
                    #### ● [高防IP(KAD)](https://docs.ksyun.com/products/4)\n
                    #### ● [DDoS原生高防](https://docs.ksyun.com/products/116)\n
                    #### ● [服务器安全(KHS)](https://docs.ksyun.com/products/41)
                    """
)

first_sentence = "#### 如需查阅金山云的相关文档可以点击下方按钮展开："
last_sentence = (
                    """
                    <style>
                        .fix-bottom {
                            margin-top: 1000px;
                        }
                    </style>
                    """,
                    """
                    <strong>如果以上文档仍然无法解决您的问题，请在右边的聊天框中输入您的问题，之后将由金山云智能小助手来为您解答😀</strong>
                    """
                 )

# 分割线
split_line = (
    """
    <style>
        .hr-twill {
            border: 0;
            padding: 3px;
            background: repeating-linear-gradient(135deg, #a2a9b6 0px, #a2a9b6 1px, transparent 1px, transparent 6px);
            transform: translateY(-50px);
            margin-bottom: -40px;
        }
    </style>
    """,
    """
        <hr class="hr-twill">
    """
)

# 圆球滚动效果
ball = (
    """
    <style>
        .box {
            position: relative;
            width: 100px;
            height: 50px;
            margin-left: 60px;
            padding-top: 15px;
        }
        .box span {
            position: absolute;width: 20px;height: 20px;background: #3498db;opacity: 0.5;border-radius: 100%;animation: anim 1s infinite ease-in-out;
        }
        .box > :nth-child(2) {
            left: 20px;animation-delay: 0.2s;
        }
        .box > :nth-child(3) {
            left: 40px;animation-delay: 0.4s;
        }
        .box > :nth-child(4) {
            left: 60px;animation-delay: 0.6s;
        }
        .box > :nth-child(5) {
            left: 80px;animation-delay: 0.8s;
        }
        .box > :nth-child(6) {
            left: 100px;animation-delay: 1.0s;
        }
        .box > :nth-child(7) {
            left: 120px;animation-delay: 1.2s;
        }
        .box > :nth-child(8) {
            left: 140px;animation-delay: 1.4s;
        }
        .box > :nth-child(9) {
            left: 160px;animation-delay: 1.6s;
        }
        @keyframes anim {
            0% {opacity: 0.3;transform: translateY(0px);}
            50% {opacity: 1;transform: translateY(-10px);background: #f9cdff;}
            100% {opacity: 0.3;transform: translateY(0px);}
        }
    </style>
    """,
    """
        <div class="box">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            <span></span>
        </div>
    """
)