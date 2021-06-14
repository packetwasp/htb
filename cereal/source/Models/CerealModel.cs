using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Cereal.Models
{
    public class CerealModel
    {
        [Required]
        public string Title { get; set; }
        [Required]
        public string Flavor { get; set; }
        [Required]
        public string Color { get; set; }
        [Required]
        public string Description { get; set; }
    }
}
