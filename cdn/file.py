from postDB import Model, Column, types


class File(Model):
    """
    File class mapped to Asset models..

    Database Attributes:
        Attributes stored in the `files` table.

        :param int id:              The file ID.
        :param str name:            The file name.
        :param str mimetype:        The files mimetype.
        :param bytes data:          The binary data (the file itself)
    """

    id = Column(types.Integer(big=True), unique=True)
    name = Column(types.String)
    mimetype = Column(types.String)
    data = Column(types.Binary)
