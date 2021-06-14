using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Cereal.Models
{
    public class Request
    {
        [Key]
        public int RequestId { get; set; }
        [Required]
        public string JSON { get; set; }
    }
}
