# Explanation: Only list the modified parts, starting with # [AAModified Start] and ending with # [AAModified End].
# 说明：仅列出修改的部分，以# [AAModified-Start]打头，# [AAModified-End]结束。

# [AAModified-Start]
# class 记录(Base):
#     __tablename__ = '记录'
#     时间 = sqlalchemy.Column(sqlalchemy.DateTime)
#     IP = sqlalchemy.Column(sqlalchemy.String(3*4+3))
#     问 = sqlalchemy.Column(sqlalchemy.Text)
#     答 = sqlalchemy.Column(sqlalchemy.Text)

class ChatRecordData(Base):
    __tablename__ = 'ChatRecord'
    Id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    RoleName = sqlalchemy.Column(sqlalchemy.Text)
    IsMine = sqlalchemy.Column(sqlalchemy.Integer)
    Time = sqlalchemy.Column(sqlalchemy.DateTime)
    IP = sqlalchemy.Column(sqlalchemy.String(3 * 4 + 3))
    Content = sqlalchemy.Column(sqlalchemy.Text)
    ChatCost = sqlalchemy.Column(sqlalchemy.Float)
# [AAModified-End]
