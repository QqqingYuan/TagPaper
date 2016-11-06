package cn.buaaqingyuan

/**
 * word count
 *
 */

import java.io.PrintWriter

import org.apache.hadoop.conf.Configuration
import org.apache.hadoop.fs.{FileSystem, Path}
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext

object WordCount {

  def main(args: Array[String]){

    if (args.length < 1) {
      System.err.println("Usage : <file>")
      System.exit(1)
    }

    val conf = new SparkConf()
    val sc = new SparkContext(conf)
    val line = sc.textFile(args(0))
    val result = line.flatMap(_.split(" ")).map((_,1)).reduceByKey(_+_).sortBy(_._2,false)
    val fs = FileSystem.get(new Configuration())
    val writer = new PrintWriter(fs.create(new Path("/data/wordcount/output")))
    result.collect().foreach( e => {
      val (k,v) = e
      writer.println(k+" "+v)
    })
    writer.close()
    sc.stop()

  }

}
