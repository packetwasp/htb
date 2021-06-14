using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net;
using System.Threading.Tasks;

namespace Cereal
{
    public class DownloadHelper
    {
        private String _URL;
        private String _FilePath;
        public String URL
        {
            get { return _URL; }
            set
            {
                _URL = value;
                Download();
            }
        }
        public String FilePath
        {
            get { return _FilePath; }
            set
            {
                _FilePath = value;
                Download();
            }
        }

        //https://stackoverflow.com/a/14826068
        public static string ReplaceLastOccurrence(string Source, string Find, string Replace)
        {
            int place = Source.LastIndexOf(Find);

            if (place == -1)
                return Source;

            string result = Source.Remove(place, Find.Length).Insert(place, Replace);
            return result;
        }

        private void Download()
        {
            using (WebClient wc = new WebClient())
            {
                if (!string.IsNullOrEmpty(_URL) && !string.IsNullOrEmpty(_FilePath))
                {
                    wc.DownloadFile(_URL, ReplaceLastOccurrence(_FilePath,"\\", "\\21098374243-"));
                }
            }
        }
    }
}
