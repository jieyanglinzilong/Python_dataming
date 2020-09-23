public static void main(String[] agrs) throws IOException {   
   FileOutputStream out = null;   
   try {   
       out = new FileOutputStream(new File("D:/a.txt"));   
       // 将你的数据，转换成某一个字符集的byte数组，然后直接写入文件即可   
       out.write("digraph{node[fontname=\"SimSun\"];开始->结束;}".getBytes("UTF-8"));   
   } catch (FileNotFoundException e) {   
       e.printStackTrace();   
   } finally {   
       out.close();   
   }   
}  