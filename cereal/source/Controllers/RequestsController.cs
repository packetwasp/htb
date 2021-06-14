using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Authorization;
using System.Linq;
using Cereal.Models;
using Cereal.Services;
using Newtonsoft.Json;
using System;

namespace Cereal.Controllers
{
    [Authorize]
    [ApiController]
    [Route("[controller]")]
    public class RequestsController : ControllerBase
    {
        [HttpPost]
        public IActionResult Create([FromBody]Request request)
        {
            using (var db = new CerealContext())
            {
                try
                {
                    db.Add(request);
                    db.SaveChanges();
                } catch {
                    return BadRequest(new { message = "Invalid request" });
                }
            }

            return Ok(new { message = "Great cereal request!", id = request.RequestId});
        }

        [Authorize(Policy = "RestrictIP")]
        [HttpGet("{id}")]
        public IActionResult Get(int id)
        {
            using (var db = new CerealContext())
            {
                string json = db.Requests.Where(x => x.RequestId == id).SingleOrDefault().JSON;
                // Filter to prevent deserialization attacks mentioned here: https://github.com/pwntester/ysoserial.net/tree/master/ysoserial
                if (json.ToLower().Contains("objectdataprovider") || json.ToLower().Contains("windowsidentity") || json.ToLower().Contains("system"))
                {
                    return BadRequest(new { message = "The cereal police have been dispatched." });
                }
                var cereal = JsonConvert.DeserializeObject(json, new JsonSerializerSettings
                {
                    TypeNameHandling = TypeNameHandling.Auto
                });
                return Ok(cereal.ToString());
            }
        }

        [Authorize(Policy = "RestrictIP")]
        [HttpGet]
        public IActionResult GetAll()
        {
            using (var db = new CerealContext())
            {
                try
                {
                    return Ok(db.Requests.ToArray().Reverse());
                }
                catch
                {
                    return BadRequest(new { message = "Invalid request" });
                }
            }
        }

        [Authorize(Policy = "RestrictIP")]
        [HttpDelete("{id}")]
        public IActionResult Delete(int id)
        {
            using (var db = new CerealContext())
            {
                try
                {
                    db.Requests.Remove(db.Requests.Where(x => x.RequestId == id).SingleOrDefault());
                    db.SaveChanges();
                    return Ok();
                }
                catch
                {
                    return BadRequest(new { message = "Invalid request" });
                }
            }
        }

        [Authorize(Policy = "RestrictIP")]
        [HttpDelete]
        public IActionResult DeleteAll()
        {
            using (var db = new CerealContext())
            {
                try
                {
                    db.Requests.RemoveRange(db.Requests.ToList());
                    db.SaveChanges();
                    return Ok();
                }
                catch
                {
                    return BadRequest(new { message = "Invalid request" });
                }
            }
        }
    }
}