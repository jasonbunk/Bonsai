class BonsaiIO
{
  typedef unsigned long long ID_t;
  BonsaiIO() {}
  ~BonsaiIO() {} 

  bool openFile(const std::string &fileName, const char mode, std::vector<ID_t> &IDList)
  { 
    assert(!isFileOpened());
    /* opens a file with "filename" and a mode "r" for read and "w" for write */
    /* if mode is "r", the indexList is populated with particle IDs from the file
     * if mode is "w", the indexList must contain unique & immutable particle IDs */
    if (mode == 'r')
      setFileIsOpenedForRead();
    else if (mode == 'w')
      setFileIsOpenedForWrite();
    else
      assert(0);
    return isFileOpened(); /* if successfull */
  }

  template<typename T>
    bool writeAttribute(const std::string &attributeName, const std::vector<T> &attributeData)
    {
      assert(isFileOpenedForWrite());
      assert(attrbiteData.size() == IDList.size());
      /* adds particle attribute, e.g.
       * writeAttribute("position", positions);
       * writeAttribute("mass", masses);
       */
      return true; /* if successful */
    }

  bool closeFile()
  {
    assert(isFileOpened());
    /* write file */
    return true; /* if successfull */
  }

  bool getAttributeList(std::vector<std::string> &attributeNameList)
  {
    assert(isFileOpenedForRead());
    /* reads attribute list from the file */
    return true;
  }

  template<typename T>
    bool readAttribute(const std::string &attributeName, std::vector<T> &attributeData)
    {
      assert(isFileOpenedForRead());
      /* returns attrbites for all particles from the list */
      return true;
    }

  template<typename T>
    bool readAttribute(const std::string &attributeName, std::vector<T> &attributeData, std::vector<ID_t> &IDList)
    {
      assert(isFileOpenedForRead());
      /* returns attrbite for particles with desired IDs */
      return true;
    }

};
