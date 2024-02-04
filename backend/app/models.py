from django.db import models


class ChatRecord(models.Model):
    localId = models.CharField(verbose_name="本地ID", max_length=255)
    talkerId = models.CharField(verbose_name="对话者ID", max_length=255)
    type = models.CharField(verbose_name="消息类型", max_length=255)
    subType = models.CharField(verbose_name="子类型", max_length=255, default=0)
    isSender = models.CharField(verbose_name="是否为发送者", max_length=255, default=False)
    createTime = models.CharField(verbose_name="创建时间", max_length=255)
    status = models.CharField(verbose_name="状态", max_length=255, null=True, blank=True)
    strContent = models.TextField(verbose_name="字符串内容", null=True, blank=True)
    strTime = models.CharField(verbose_name="字符串时间", max_length=20)
    remark = models.CharField(
        verbose_name="备注", max_length=255, null=True, blank=True)
    nickName = models.CharField(
        verbose_name="昵称", max_length=255, null=True, blank=True)
    sender = models.IntegerField(verbose_name="发送者", null=True, blank=True)

    class Meta:
        verbose_name = "聊天记录"
        verbose_name_plural = "聊天记录"
